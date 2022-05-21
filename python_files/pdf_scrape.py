import pandas as pd
import PyPDF2


global final_scraped_numbers_list
global school_order_list
global ethnicity_order_list
global year_list
final_scraped_numbers_list = []
school_order_list = []
ethnicity_order_list = ['Black or African American', 'Asian', 'American Indian or Native Alaskan', 'White', 'Native Hawaiian or Pacific Islander', 'Two or more races', 'Hispanic/Latino']
year_list = ['2019', '2018', '2017', '2016']

def pdf_page3_scrape(file):
    pdf_file = open(file, 'rb')
    pdf_read = PyPDF2.PdfFileReader(pdf_file)
    pdf_page_obj = pdf_read.getPage(3)
    pdf_page_text = pdf_page_obj.extractText()
    pdf_file.close()
    pdf_page_text_cleaned = pdf_page_text.replace('\n', ' ')
    substring1 = 'AM'
    substring2 = '# of students in cohort'
    substring3 = '% of students meeting outcome'
    start_index = pdf_page_text_cleaned.find(substring1)
    substring2_index_list = [i for i in range(len(pdf_page_text_cleaned)) if pdf_page_text_cleaned.startswith(substring2, i)]
    del substring2_index_list[-1]
    del substring2_index_list[6]
    substring3_index_list = [i for i in range(len(pdf_page_text_cleaned)) if pdf_page_text_cleaned.startswith(substring3, i)]
    list_of_data_substrings = []
    list_of_data_substrings.append(pdf_page_text_cleaned[start_index+2:substring3_index_list[0]])
    for i in range(len(substring2_index_list)):
        list_of_data_substrings.append(pdf_page_text_cleaned[substring2_index_list[i]+ len(substring2):substring3_index_list[i+1]])
    new_list_of_data_substrings = []
    for old_string in list_of_data_substrings:
        for substr in ethnicity_order_list:
            if substr in old_string:
                new_list_of_data_substrings.append(old_string.replace(substr,''))
    new_list_of_data_substrings = new_list_of_data_substrings[5:]
    new_list_of_data_substrings[0] = new_list_of_data_substrings[0][34:]
    for i in range(len(new_list_of_data_substrings)):
        new_list_of_data_substrings[i] = new_list_of_data_substrings[i].strip().split()
        new_list_of_data_substrings[i] = new_list_of_data_substrings[i][3:15]
    return new_list_of_data_substrings


def pdf_page2_scrape(file):
    pdf_file = open(file, 'rb')
    pdf_read = PyPDF2.PdfFileReader(pdf_file)
    pdf_page_obj = pdf_read.getPage(2)
    pdf_page_text = pdf_page_obj.extractText()
    pdf_file.close()
    pdf_page_text_cleaned = pdf_page_text.replace('\n', ' ')
    substring1 = 'AM Total Number of Students in Class'
    substring2 = '# of students in cohort'
    substring3 = '% of students meeting outcome'
    start_index = pdf_page_text_cleaned.find(substring1)
    substring2_index_list = [i for i in range(len(pdf_page_text_cleaned)) if pdf_page_text_cleaned.startswith(substring2, i)]
    substring2_index_list = substring2_index_list[0:2]
    substring3_index_list = [i for i in range(len(pdf_page_text_cleaned)) if pdf_page_text_cleaned.startswith(substring3, i)]
    list_of_data_substrings = []
    list_of_data_substrings.append(pdf_page_text_cleaned[start_index+len(substring1):substring3_index_list[0]])
    for i in range(len(substring2_index_list)):
        list_of_data_substrings.append(pdf_page_text_cleaned[substring2_index_list[i]+ len(substring2):substring3_index_list[i+1]])
    new_list_of_data_substrings = [list_of_data_substrings[0]]
    for old_string in list_of_data_substrings:
        for substr in ethnicity_order_list:
            if substr in old_string:
                new_list_of_data_substrings.append(old_string.replace(substr,''))
    for i in range(len(new_list_of_data_substrings)):
        new_list_of_data_substrings[i] = new_list_of_data_substrings[i].strip().split()
        new_list_of_data_substrings[i] = new_list_of_data_substrings[i][3:15]
    return new_list_of_data_substrings


def pdf_scrape(file):
    target = 'College'
    target_index = file.find(target)
    school_name = file[:target_index-1]
    school_order_list.append(school_name)
    page2 = pdf_page2_scrape(file)
    page3 = pdf_page3_scrape(file)
    scraped_join = page2 + page3
    final_scraped_numbers_list.append(scraped_join)
    print(f'{file} has been scraped and added into global lists')


def create_table():
    final_table = pd.DataFrame()
    for i in range(len(final_scraped_numbers_list)):
        for j in range(len(final_scraped_numbers_list[i])):
            for k in range(4):
                table_dict = {}
                table_dict['SchoolName'] = school_order_list[i]
                print(school_order_list[i])
                table_dict['Ethnicity'] = ethnicity_order_list[j]
                print(ethnicity_order_list[j])
                table_dict['ClassYear'] = year_list[k-1]
                table_dict['PercentAcceptance'] = final_scraped_numbers_list[i][j][(k*3)]
                table_dict['NumberAcceptance'] = final_scraped_numbers_list[i][j][(k*3)+1]
                table_dict['StudentTotal'] = final_scraped_numbers_list[i][j][(k*3)+2]
                final_table = final_table.append(table_dict, ignore_index=True)
    return final_table


pdf_scrape('East HS College Attendance Disaggregated Fall 2021.pdf')
print(final_scraped_numbers_list)
pdf_scrape('Lincoln High College Attendance Disaggregated Fall 2021.pdf')

pdf_scrape('North Star HS College Attendance Disaggregated Fall 2021.pdf')

pdf_scrape('Northeast HS College Attendance Disaggregated Fall 2021.pdf')

pdf_scrape('Southeast HS College Attendance Disaggregated Fall 2021.pdf')

pdf_scrape('Southwest HS College Attendance Disaggregated Fall 2021.pdf')

export_table = create_table()
export_table.to_csv('CollegeAcceptanceScraped.csv', index=False)



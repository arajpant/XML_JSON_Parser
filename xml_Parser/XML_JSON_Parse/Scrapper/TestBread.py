# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import csv

#
# def parse_row(url):
#     # global data_list
#     # each_breadcrum_string = ''
#     # each_store_id = row['StoreId']
#     # each_product_sku = row['ProductSKU']
#     # each_url = row['ProductURL']
#
#     each_url = url
#
#
#     each_url = each_url.strip()
#     source_code = requests.get(each_url)
#     soup = BeautifulSoup(source_code.text, 'html.parser')
#
#
#
#     url_result_set = soup.find_all('url')
#     category_url_list = []
#     for url_result in (url_result_set):
#         url = url_result.find('loc').text
#         priority = url_result.find('priority').text
#         # print (url)
#         # print (priority)
#         if (priority == '0.5'):
#             print(url)
#             category_url_list.append(url)
#
#
#
#     print (len(category_url_list))
#     exit()
#
#     for each_text in a[0].find_all('a'):
#         each_text = each_text.text
#         each_text = str(each_text).strip()
#         each_breadcrum_list.append(each_text)
#
#     # #for last breadCrumb
#     # for each_text in a[0].find_all('li', {'class':'item product'}):
#     #     each_text = each_text.text
#     #     each_text = str(each_text).strip()
#     #     each_breadcrum_list.append(each_text)
#
#     # a is list so we take a[0] as it has only one element
#     #this also works
#     #this each_item is single tag so no need to do loop
#     # for each_item in soup.find_all("div", {"class" : "crumbs clearfix"}):
#     #     for each_text in each_item.find_all('div')[1].find_all('a'):
#     #         print(each_text.text)
#     #     print(each_item)
#     #############################################################################
#     #
#     # for each_text in a[0].find_all('div')[1].find_all('a'):
#     #     each_text = each_text.text
#     #     each_text = str(each_text).strip()
#     #     each_breadcrum_list.append(each_text)
#     #
#     each_breadcrum_string = ' > '.join(each_breadcrum_list)
#     each_breadcrum_string = each_breadcrum_string.strip()
#     print(each_breadcrum_string)
#     exit()
#
#
# if __name__ == '__main__':
#
#     parse_row('https://www.leadinglady.com/sitemap.xml')
#

 ########################################################################################################################################################




import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

from lxml import html
import requests


def parse_row(url):
    global data_list
    each_url = url
    each_url = each_url.strip()
    source_code = requests.get(each_url)
    soup = BeautifulSoup(source_code.content, "lxml")

    # print(soup)
    # exit()

    # page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    # tree = html.fromstring(page.content)
    #
    # test = tree.xpath('//div[@class="crambsDib"]/div[1]/text()')
    # print(test)
    # exit()


    # print(soup)

################################################################################################################################
    #Amazon

    # check_strike = soup.find_all('span', {'class': 'a-text-strike'})
    # # check_availability = soup.find_all('div', {'id':'availability'})[0].find_all('span', {'class':'a-size-medium a-color-price'})
    # check_availability = soup.find_all('div', {'id':'availability'})
    # #
    # # print(check_strike)
    # # print(check_availability)
    #
    # # check_availability = soup.find_all('span', {'class': 'a-size-medium a-color-price'})
    # # print(check_strike)
    # # print(type(check_strike))
    # # print(len(check_strike))
    # if (len(check_strike) != 0):
    #     for i in check_strike:
    #         check_strike_text = i.text
    #         check_strike_text = check_strike_text.strip()
    #         print(check_strike_text)
    #         print('-----------')
    # else:
    #     for each1 in check_availability:
    #         for each2 in each1.find_all('span', {'class': 'a-size-medium a-color-price'}):
    #             check_availability_text = each2.text
    #             check_availability_text = check_availability_text.strip()
    #             print(check_availability_text)
    #             print('-----------')
    # exit()

  #######################################################################################
    # #Canopies and traps
    # each_breadcrum_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs-container container'})
    # # # for each_text in breadcrumb_set[0].find_all('a'):
    #     each_text = each_text.text
    #     each_text = str(each_text).strip()
    #     each_breadcrum_list.append(each_text)
    #
    # #for last breadCrumb
    # for each_text in breadcrumb_set[0].find_all('span', {'class':'lastCrumb'}):
    #     each_text = each_text.text
    #     each_text = str(each_text).strip()
    #     each_breadcrum_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(each_breadcrum_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_url)
    # print(each_breadcrumb_string)
    # exit()


  ##########################################################################################

    #just for jeeps #####################################################################################################

    # breadcrumb_set=soup.find('div',{'class':'breadcrumbs'})

    # breadcrumb_set = breadcrumb_set.text
    # each_breadcrum_string = breadcrumb_set.strip()
    # print(each_breadcrum_string)
    # print(type(each_breadcrum_string))
    # print(len(each_breadcrum_string))
    # exit()

    # OR for just for jeeps
########################################################################################3
    # for each_text in breadcrumb_set[0].find_all('a'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     print(each_text)
    #     breadcrumb_list.append(each_text)
    #     # print(each_text)

    # for last breadcrumb
    # last_breadcrumb = breadcrumb_set[0]
    # last_breadcrumb = last_breadcrumb.contents[-1][3:]
    # breadcrumb_list.append(last_breadcrumb)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

#     #Paper lantern
# #####################################################################################################################
#     breadcrumb_list = []
#     breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs'})
#
#     for each_text in breadcrumb_set[0].find_all('a'):
#         each_text = each_text.text
#         each_text = each_text.strip()
#         breadcrumb_list.append(each_text)
#
#
#     # for last breadcrumb
#     last_breadcrumb = breadcrumb_set[0]
#     last_breadcrumb = last_breadcrumb.contents[-3]
#     last_breadcrumb = last_breadcrumb.strip()
#     breadcrumb_list.append(last_breadcrumb)
#
#     each_breadcrumb_string = ' > '.join(breadcrumb_list)
#     each_breadcrumb_string = each_breadcrumb_string.strip()
#     print(each_breadcrumb_string)
#     exit()

###################################################################################################################
    # NSCD
    # #####################################################################################################################
    breadcrumb_list = []
    breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs'})
    breadcrumb_set = breadcrumb_set[0].text
    each_breadcrum_string = breadcrumb_set.strip()
    print(each_breadcrum_string)
    print(type(each_breadcrum_string))
    print(len(each_breadcrum_string))
    exit()
    # #
    # ###################################################################################################################

    # each_breadcrum_list = []
    # all = soup.find_all("div", {"class": "kuName"})
    # # each_href = all.find_all('a')['href']
    # print(all)
    # exit()
    # # print(type(all))
    # # each_text = all[0].text
    # # print(each_text)
    # # exit()
    # # all is list so we take all[0] as it has only one element
    # # this also works
    # # this each_item is single tag so no need to do loop
    # # for each_item in soup.find_all("div", {"class" : "crumbs clearfix"}):
    # #     for each_text in each_item.find_all('div')[1].find_all('a'):
    # #         print(each_text.text)
    # #     print(each_item)
    # #############################################################################
    #
    # for each_text in all[0].find_all('a')['href']:
    #     each_text = each_text.text
    #     each_text = str(each_text).strip()
    #     each_breadcrum_list.append(each_text)
    #
    # each_breadcrum_string = ' > '.join(each_breadcrum_list)
    # each_breadcrum_string = each_breadcrum_string.strip()
    # print(each_breadcrum_string)

#############################################################################################################################3333
    #Cool Jams
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs crumbs'})
    #
    # for each_text in breadcrumb_set[0].find_all('a'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     # print(each_text)
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # print(each_breadcrumb_string)
    #
    # exit()
# ######################################################################################################################
# # #     #Chicago computer supply
     # breadcrumb_list = []
     # breadcrumb_set = soup.find_all('div', {'class': 'scBreadcrumbs'})

     # each_breadcrumb_string = breadcrumb_set[0].text
     # each_breadcrumb_string = each_breadcrumb_string.strip()
     # print(each_breadcrumb_string)
     # exit()


    ############################################################################################################

    #
    # #World Wide Chocolate
    # #
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs'})
    #
    # for each_text in breadcrumb_set[0].find_all('a'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # # for last breadcrumb
    # last_breadcrumb = breadcrumb_set[0].find_all('li')[-1]
    # last_breadcrumb = last_breadcrumb.text
    # last_breadcrumb = last_breadcrumb.strip()
    # breadcrumb_list.append(last_breadcrumb)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

    #Candy Apple Costumes
####################################################################################################
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs'})
    
    # breadcrumb_set = breadcrumb_set[0].text
    # each_breadcrum_string = breadcrumb_set.strip()
    # print(each_breadcrum_string)
    # print(type(each_breadcrum_string))
    # print(len(each_breadcrum_string))
    # exit()
######################################################################################################

    # # #Car and truck remotes
    #
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'cycBreadcrumbs'})
    #
    # for each_text in breadcrumb_set[0].find_all('a'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # # for last breadcrumb
    # for each_text in breadcrumb_set[0].find_all('span', {'class': 'cyclastCrumb'}):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

#######################################################################################################################
  # #Greek Gear
  #
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs-container container'})
    #
    # for each_text in breadcrumb_set[0].find_all('a'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # # for last breadcrumb
    # for each_text in breadcrumb_set[0].find_all('span', {'class': 'lastCrumb'}):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()


#######################################################################################################################
  # Sharper Uniforms
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'scBreadcrumbs'})
    # each_breadcrumb_string = breadcrumb_set[0]
    # each_breadcrumb_string = each_breadcrumb_string.text
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)

    # exit()
#####################################################################################################################################################

# # A1 Traps
#
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs-container container'})
    #
    # for each_text in breadcrumb_set[0].find_all('a'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # # for last breadcrumb
    # for each_text in breadcrumb_set[0].find_all('span', {'class': 'lastCrumb'}):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

#######################################################################################################################

# SEE

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx
    # # Affordable lamps

    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'crumbs clearfix'})
    # # breadcrumb_set = breadcrumb_set[0].contents[1]
    # each_breadcrumb_string= breadcrumb_set[0].text
    # # for each_text in breadcrumb_set[0].find_all('a'):
    # #     each_text = each_text.text
    # #     each_text = each_text.strip()
    # #     breadcrumb_list.append(each_text)
    # #
    # # for each_text in breadcrumb_set[0].find_all('strong'):
    # #     each_text = each_text.text
    # #     each_text = each_text.strip()
    # #     breadcrumb_list.append(each_text)
    # #
    # # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.replace(' / ',' > ').strip()
    # print(each_breadcrumb_string)
    # exit()
    # #
    # #######################################################################################################################

    # #Titanium Jewelry
    # #Titanium Jewelry
    #

    #
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs'})
    
    # for each_text in breadcrumb_set[0].find_all('a'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

    #######################################################################################################################
 # #Brilliant Outdoors
 #
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'crambsDib'})
    # breadcrumb_set = breadcrumb_set[0]
    # breadcrumb_set = breadcrumb_set.find_all('div')
    # breadcrumb_set = breadcrumb_set[0]
    #
    #
    # for each_text in breadcrumb_set.find_all('a'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

#######################################################################################################################################################
    # # framedisplays
    #
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'eyBreadcrumbs'})
    #
    # for each_text in breadcrumb_set[0].find_all('a'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # #for lastcrumb
    # lastcrumb = breadcrumb_set[0].find_all('span',{'class':'lastCrumb'})
    # lastcrumb = lastcrumb[0]
    # lastcrumb = lastcrumb.text
    # lastcrumb = lastcrumb.strip()
    # breadcrumb_list.append(lastcrumb)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()
#######################################################################################################################################
    # # Westech Rigging Supply
    #
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs'})
    #
    # for each_text in breadcrumb_set[0].find_all('a'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

#######################################################################################################################################
    # Yates Jewelry

    #breadcrumb_list = []
    #breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs'})
    #if len(breadcrumb_set)==0:
    #    breadcrumb_set = soup.find_all('article', {'id': 'breadcrumbs'})
    #    each_breadcrumb_string=breadcrumb_set[0].text
    #    each_breadcrumb_string=each_breadcrumb_string.strip()

    #    each_breadcrumb_string=each_breadcrumb_string.replace('|',' > ')

    #    print(each_breadcrumb_string)
    
        
        
    #else:     
    #    for each_text in breadcrumb_set[0].find_all('a'):
    #        each_text = each_text.text
    #        each_text = each_text.strip()
    #        breadcrumb_list.append(each_text)
        
    #    #for lastcrumb
    #    each_text = breadcrumb_set[0].find('span', {'class':'lastname'})
    #    each_text = each_text.text
    #    breadcrumb_list.append(each_text)
        
    #    each_breadcrumb_string = ' > '.join(breadcrumb_list)
    #    each_breadcrumb_string = each_breadcrumb_string.strip()
    #    print(each_breadcrumb_string)
    
    #exit()

#######################################################################################################################################
# Aloha funwear
#
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('ol', {'class': 'breadcrumb'})
    #
    # for each_text in breadcrumb_set[0].find_all('li'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

############################################################################################################################

    # #mex
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('ul', {'class': 'breadcrumbs'})
    #
    # for each_text in breadcrumb_set[0]:
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

########################################################################################33
    # #cnsdisplays
    # breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs'})
    # each_breadcrumb_string = breadcrumb_set[0]
    # each_breadcrumb_string = each_breadcrumb_string.text
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()
    #

############################################################################################
    # # #controller Chaos
    # breadcrumb_list = []
    # breadcrumb_set = soup.find('div', {'class':'breadcrumbs'})
    # each_breadcrumb_string = breadcrumb_set.text.replace('  >  ', ' > ').replace("&nbsp", "").strip()
    #
    # print(each_breadcrumb_string)
    # print(type(each_breadcrumb_string))
    # print(len(each_breadcrumb_string))
    # exit()

    ################################################################################
    #
    # #Suspender Store
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('ul', {'class': 'breadcrumbs'})
    #
    # for each_text in breadcrumb_set[0].find_all('li'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()
    #
    #
############################################################################################

    # #Leading leady
    # Description
    #
    # breadcrumb_set = soup.find('div', {'class': 'long_description hide'})
    # breadcrumb_set = breadcrumb_set.text
    # print(breadcrumb_set)
    # exit()
    #
    ############################################################################################################################

    # #11x17
    # breadcrumb_list = []
    # breadcrumb_set = soup.find('div', {'id': 'breadcrumbs-wrapper'})
    # for each_text in breadcrumb_set.find_all('li'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

    ############################################################################################################################

    # Vitabath
    # sku = soup.find('span', {'class': 'VariationProductSKU'})
    # sku = sku.text.strip()
    # print(sku)
    # exit()
    #
    # breadcrumb_list = []
    # breadcrumb_set = soup.find('ul', {'class': 'breadcrumbs'})
    # for each_text in breadcrumb_set.find_all('li'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    #
    # for each_product in  soup.find_all('a',{'class': 'overlay-link'}):
    #     each_product = each_product['href'].strip()
    #     print(each_product)
    #
    # exit()
        # each_text = each_text.text
        # each_text = each_text.strip()
        # breadcrumb_list.append(each_text)

    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

############################################################################################################################

    # GustusVitae


    # breadcrumb_list = []
    # breadcrumb_set = soup.find('ul', {'class': 'breadcrumbs'})
    # for each_text in breadcrumb_set.find_all('li'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

    ############################################################################################################################

    # # CalExotics

    # breadcrumb_list = []
    # breadcrumb_set = soup.find('div', {'class': 'breadcrumbs'})
    # for each_text in breadcrumb_set.find_all('li'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()



    ############################################################################################################################

    # # ManyBidets
    #
    # breadcrumb_list = []
    # breadcrumb_set = soup.find('div', {'id': 'breadcrumbs-wrapper'})
    # for each_text in breadcrumb_set.find_all('li'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

    ############################################################################################################################

    # Julep
    #
    # breadcrumb_list = []
    # breadcrumb_set = soup.find('div', {'class': 'breadcrumbs-container'})
    # for each_text in breadcrumb_set.find_all('li'):
    #     if each_text.text:
    #         each_text = each_text.text.replace('|','').replace("&nbsp;", "")
    #         each_text = each_text.strip()
    #         breadcrumb_list.append(each_text)
    #     else:
    #         continue
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()
    #

    #
    # breadcrumb_list = []
    # breadcrumb_set = soup.find('div', {'class': 'category-products'})
    # for each_text in breadcrumb_set.find_all('a',{'class': 'product-name'}):
    #     # each_text = each_text.text.replace('|','')
    #     each_text = each_text.find('div', {'class':'name'}).text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # print(breadcrumb_list)
    # # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # # each_breadcrumb_string = each_breadcrumb_string.strip()
    # # print(each_breadcrumb_string)
    # exit()


    ############################################################################################################################

    # Socksrock
    # base_url = 'https://www.socksrock.com'
    # product_grid = soup.find('div', {'id': 'bc-sf-filter-products'})
    # for each_product in product_grid.find_all('div',{'class':'item'}):
    #     each_sku = each_product.find('a')['href'].strip().split('/')[-1]
    #     print(each_sku)
    #     each_product = '{}{}'.format(base_url,each_product.find('a')['href'].strip())
    #     print(each_product)
    # exit()
    #
    ############################################################################################################################

    # LAPG
    # breadcrumb_list = []
    # breadcrumb_set = soup.find('div', {'class': 'breadcrumbs'})
    # for each_text in breadcrumb_set.find_all('li'):
    #     each_text = each_text.text.replace("&nbsp", "")
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

    # ############################################################################################################################
    #
    # # LAPG
    # breadcrumb_list = []
    # breadcrumb_set = soup.find('div', {'class': 'breadcrumbs'})
    # for each_text in breadcrumb_set.find_all('li'):
    #     each_text = each_text.text.replace("&nbsp", "").replace('/ ', '')
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()



############################################################################################################################

    # LAPG
    # breadcrumb_list = []
    # breadcrumb_set = soup.find('div', {'class': 'breadcrumbs'})
    # print(soup)
    # exit()
    # for each_text in breadcrumb_set.find_all('li'):
    #     each_text = each_text.text.replace("&nbsp", "").replace('/ ', '')
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

    ############################################################################################################################
    #Stetgescope
    #
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('ul', {'class': 'breadcrumbs'})
    #
    # # print(breadcrumb_set)
    #
    # for each_text in breadcrumb_set[0].find_all('a'):
    #     each_text = each_text.text
    #     each_text = each_text.strip()
    #     breadcrumb_list.append(each_text)
    #
    # each_breadcrumb_string = ' > '.join(breadcrumb_list)
    # each_breadcrumb_string = each_breadcrumb_string.strip()
    # print(each_breadcrumb_string)
    # exit()

##################################################################################################################################
    #Pillows
    # breadcrumb_list = []
    # breadcrumb_set = soup.find_all('div', {'class': 'breadcrumbs'})
    
    # each_breadcrumb_string = breadcrumb_set[0].text
    # each_breadcrumb_string = each_breadcrumb_string.replace('//','>').strip()
    # print(each_breadcrumb_string)
    # exit()

###################################################################################################################################
    #IndependentLiving
    #breadcrumb_list = []
    
    #breadcrumb_set = soup.find('div', {'id': 'breadcrumb'})
    
    #for each_text in breadcrumb_set.find_all('a'):
        #text=each_text.text.strip()
        #breadcrumb_list.append(text)
    
    ##lastcrumb
    #index=breadcrumb_set.contents[-1].find('/')+1
    #breadcrumb_list.append(breadcrumb_set.contents[-1][index:].strip())
    
    
    
    #each_breadcrumb_string = ' > '.join(breadcrumb_list)
    #each_breadcrumb_string = each_breadcrumb_string.strip()
    #print(each_breadcrumb_string)

    #exit()

###################################################################################################################################
    #Lehman
    #breadcrumb_list = []
    
    #breadcrumb_set = soup.find('div', {'id': 'breadcrumb'})
    
    #for each_text in breadcrumb_set.find_all('a'):
    #    text=each_text.text.strip()
    #    breadcrumb_list.append(text)
    
    ##lastcrumb
    #breadcrumb_list.append(breadcrumb_set.contents[-1].strip())
    
    
    
    #each_breadcrumb_string = ' > '.join(breadcrumb_list)
    #each_breadcrumb_string = each_breadcrumb_string.strip()
    #print(each_breadcrumb_string)

    #exit()
#####################################################################################################################################
    #Vinyl Disorder
    
    # breadcrumb_set=soup.find('div' ,{'class':'scBreadcrumbs'})

    # each_breadcrumb_string=breadcrumb_set.text.strip()
    # print(each_breadcrumb_string)

    # exit()

############################################################################################################################################
    #Q source
    # breadcrumb_set=soup.find('div', {'class':'detail-breadcrumbs'})
    
    # each_breadcrumb_string=breadcrumb_set.text.strip().replace('»','>')

    # print(each_breadcrumb_string)

    # exit()

############################################################################################################################################
    # Curls
    
    # breadcrumb_set=[]

    # breadcrumb_class=soup.find('div', {'class':'breadcrumbs'})
    # breadcrumb_text=breadcrumb_class.find_all('a')

    # for each_item in breadcrumb_text:
    #     breadcrumb_set.append(each_item.text.strip())

    # each_breadcrumb_string = ' > '.join(breadcrumb_set)
    # print(each_breadcrumb_string)

    # exit()


############################################################################################################################################
    # Fjorn

    # breadcrumb_div=soup.find('div',{'id':'breadcrumbs'})
    
    # breadcrumb_set=breadcrumb_div.find('div', recursive=False)
    
    # for div in breadcrumb_set.find_all('div'):
    #     div.decompose()

    # breadcrumb_text=breadcrumb_set.text.strip().replace('|','>')
    # print(breadcrumb_text)

    # quit()

############################################################################################################################################
    # Marys Tack

    # breadcrumb_set=[]
    # breadcrumb_class= soup.find('ul',{'class':'breadcrumbs'})

    # for each_text in breadcrumb_class.find_all('li'):
    #     breadcrumb_set.append(each_text.text.strip())

    # each_breadcrumb_string = ' > '.join(breadcrumb_set)

    # print(each_breadcrumb_string)

    # quit()

############################################################################################################################################


if __name__ == '__main__':
    data_list = []

    parse_row('https://marystack.com/abree-equestrian-bracelet/')
    output_df = pd.DataFrame(data_list, columns=columns)
    print(output_df)



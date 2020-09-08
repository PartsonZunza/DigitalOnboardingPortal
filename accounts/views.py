from tkinter import Image

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, CreatingMyUserForm, UploadFileForm, OnBoardingPortal
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import json
import base64
import re


# selected_id = ''


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreatingMyUserForm()
        if request.method == 'POST':
            form = CreatingMyUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:

                messages.warning(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    def getJSON(filePathAndName):
        with open(filePathAndName, 'r') as fp:
            return json.load(fp)

    products_data = getJSON('./data.json')

    # api stuff
    # products = []
    # api_token = "0cc4ebe9-3f7e-4766-9b14-6b49385b53d3"
    # api_endpoint = "http://196.216.224.167:8080/handler/api/all-products"
    # headers = {'Authorization': 'Bearer' + api_token,
    #            'Content-Type': 'application/json; charset=utf-8',
    #            }
    # api_data = requests.get(api_endpoint, headers=headers)
    # json_data = json.loads(api_data.text)
    #
    # for i in range(0, len(json_data) - 1):
    #     products.append(
    #         {
    #             'product_name': json_data[i]['productName'],
    #             'short_description': json_data[i]['productName']
    #         }
    #     )

    #
    # orders = Order.objects.all()
    # customers = Customer.objects.all()
    #
    # total_customers = customers.count()
    #
    # total_orders = orders.count()
    # delivered = orders.filter(status='Delivered').count()
    # pending = orders.filter(status='Pending').count()

    # context = {'orders': orders, 'customers': customers,
    #            'total_orders': total_orders, 'delivered': delivered,
    #            'pending': pending
    #            }
    total_products = len(products_data)
    products = []
    for i in range(0, 5):
        products.append(
            {
                'productName': products_data[i]['productName'],
                'applicableCurrencies': products_data[i]['applicableCurrencies']
            }
        )

    newproduct = OnBoardingPortal.new_product
    context = {'products': products, 'total_products': total_products,'new_products':newproduct}

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def products_view(request):
    def getJSON(filePathAndName):
        with open(filePathAndName, 'r') as fp:
            return json.load(fp)

    products_json = getJSON('./test.json')
    context = {'products_json': products_json}

    return render(request, 'accounts/products.html', context)


@login_required(login_url='login')
def product_view(request, id):
    context = {'id': id}

    def getJSON(filePathAndName):
        with open(filePathAndName, 'r') as fp:
            return json.load(fp)

    products = []
    product_id = []
    products_details = []
    products_image = []
    products_Terms = []
    products_Conditions = []
    products_full_Description = []
    products_MinimumRequirements = []
    products_Code = []
    # product_Currency
    product_shortdescription = []
    wanted_product = id
    selected_id = id

    # custom products
    address = []
    City = []
    country = []
    flat = []
    other = []

    # conditions

    # whatYouNeed
    whatYouCanDo = []
    htmlpage = []
    priority = []
    lightKYC = []


    products_data = getJSON('./test.json')

    for i in range(0, len(products_data) ):

        if products_data[i]['id'] == selected_id:
            products.append(
                {

                    products_data[i]['id'],

                }

            )
            products_details.append(
                {

                    products_data[i]['productName'],
                })

            product_shortdescription.append({

                products_data[i]['shortDescription'],
            }
            )
            products_image.append({

                products_data[i]['imageUrl'],
            }
            )
            products_Terms.append({

                products_data[i]['productTerms'],
            }
            )
            products_Conditions.append({

                products_data[i]['productConditions'],
            }
            )

            products_full_Description.append({

                products_data[i]['fullDescription'],
            }
            )

            products_MinimumRequirements.append({

                products_data[i]['productMinimumRequirements'],
            }
            )

            products_Code = products_data[i]['productCode']
            product_Currency = products_data[i]['applicableCurrencies']
            customFields = products_data[i]['customFields']

            # Conditions
            whatYouNeed = products_data[i]['whatYouNeed']
            whatYouCanDo = products_data[i]['whatYouCanDo']
            htmlpage = products_data[i]['htmlPage']
            priority = products_data[i]['priority']
            lightKYC = products_data[i]['lightKyc']

            # try:
            if wanted_product in products[len(products) - 1]:

                def convert_list_to_string(org_list, seperator=''):
                    return seperator.join(org_list)

                products_Terms = convert_list_to_string(products_Terms[0])
                products_Conditions = convert_list_to_string(products_Conditions[0])
                products_MinimumRequirements = convert_list_to_string(products_MinimumRequirements[0])


                if products_image[0] == 'null':
                    full_str = 'null'
                else:
                    full_str = convert_list_to_string(products_image[0])

                if len(products_details[0]) >= 5:
                    product_name = 'null'
                else:
                    product_name = convert_list_to_string(products_details[0])

                if len(product_shortdescription[0]) >= 5:
                    shortdescription = 'null'
                else:
                    shortdescription = convert_list_to_string(product_shortdescription[0])

                if len(products_full_Description[0]) <= 10:

                    products_full_Description = 'None'

                else:
                    products_full_Description = convert_list_to_string(products_full_Description[0])

                if products_Code == 'null ':

                    products_Code = 'null'
                else:
                    products_Code


                if whatYouNeed is None:
                    whatYouNeed = 'None'
                else:
                    whatYouNeed = convert_list_to_string(whatYouNeed[0])

                if whatYouCanDo is None:
                    whatYouCanDo = 'None'
                else:
                    whatYouCanDo = convert_list_to_string(whatYouCanDo[0])

                if product_Currency is None:
                    product_currency = 'None'
                else:
                    product_currency = convert_list_to_string(product_Currency[0])

                prod_id = convert_list_to_string(products[0])

                context = {'id': products[0],
                           'product_details': product_name,
                           'product_shortdescription': shortdescription,
                           'products_image': full_str,
                           'products_Terms': products_Terms,
                           'products_Conditions': products_Conditions,
                           'products_full_Description': products_full_Description,
                           'products_MinimumRequirements': products_MinimumRequirements,
                           'products_Code': products_Code,
                           'product_Currency': product_currency,
                           'product_need': whatYouNeed,
                           'product_do': whatYouCanDo,
                           'product_page': htmlpage,
                           'product_priority': priority,
                           'product_kyc': lightKYC,
                           'product_id': prod_id,

                           }


            else:
                print('did not execute context')

        else:
            print('not found ')

    return render(request, 'accounts/product_view.html', context)


@login_required(login_url='login')
def update_product(request):
    if request.method == 'POST':


        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_terms = request.POST.get('product_terms')
        product_conditions = request.POST.get('product_conditions')
        product_code = request.POST.get('product_code')
        product_currency = request.POST.get('product_currency')
        product_kyc = request.POST.get('product_kyc')
        product_requirements = request.POST.get('product_minimum')
        product_need = request.POST.get('product_need')
        product_do = request.POST.get('product_do')
        product_priority = request.POST.get('product_priority')


        try:

            with open('test.json', 'r+') as jsonFile:
                data = json.load(jsonFile)

                my_gen = (item for item in data if item['id'] == product_id)
                for item in my_gen:
                    print(item)
                item["productName"] = product_name
                item["shortDescription"] = product_description
                item["productTerms"] = product_terms
                item["productConditions"] = product_conditions
                item["fullDescription"] = product_description
                item["productMinimumRequirements"] = product_requirements
                item["productCode"] = product_code
                item["applicableCurrencies"] = [product_currency]
                item["whatYouNeed"] = [product_need]
                item["whatYouCanDo"] = [product_do]
                item["priority"] = product_priority
                item["lightKyc"] = product_kyc


                jsonFile.seek(0)  # rewind
                json.dump(data, jsonFile)
                jsonFile.truncate()

                return render(request, 'accounts/updateSuccess.html')


        except Exception as ex:
            print(ex, 'Occured')


    else:
        print('Failed')

    context = {'product_name': product_name, 'product_description': product_description,
                'product_terms': product_terms,
               'product_conditions': product_conditions, 'product_requirements': product_requirements,
               'product_code': product_code, 'product_currency': product_currency

               }

    return render(request, "accounts/products.html", context)


@login_required(login_url='login')
def reports(request):

    def getJSON(filePathAndName):
        with open(filePathAndName, 'r') as fp:
            return json.load(fp)

    products_data = getJSON('./data.json')
    total_products = len(products_data)

    products = []
    for i in range(0, 5):
        products.append(
            {
                'productName': products_data[i]['productName'],
                'applicableCurrencies': products_data[i]['applicableCurrencies']
            }
        )

    newproduct=OnBoardingPortal.new_product

    context = {'products': products, 'total_products': total_products,'new_product': newproduct}


    return render(request, 'accounts/reports.html', context)


@login_required(login_url='login')
def find(request):
    context={}
    try:
        if request.method == 'GET':

            search_item = request.GET.get('searchitem')

            with open('test.json', 'r+') as jsonFile:
                data = json.load(jsonFile)

                my_gen = (item for item in data if item['productCode'] == search_item)

                if my_gen:

                    for item in my_gen:

                        product_name =item['productName']
                        product_short = item['shortDescription']
                        product_id = item['id']

                else:
                    print('Could not find code')
                jsonFile.seek(0)  # rewind
                json.dump(data, jsonFile)
                jsonFile.truncate()

            context = {'product_name': product_name,'product_short':product_short,'product_id':product_id}
    except Exception as ex:
        print(ex)

    return render(request, 'accounts/find.html', context)


@login_required(login_url='login')
def product_add(request):

    try:
        if request.method == 'POST' and request.FILES['product_image']:
            myfile = request.FILES['product_image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)

            product_name = request.POST.get('first_name')
            product_description = request.POST.get('description')
            product_terms = request.POST.get('product_terms')
            product_conditions = request.POST.get('product_conditions')
            product_code = request.POST.get('last_name')
            product_currency = request.POST.get('currency')
            product_kyc = request.POST.get('kyc')
            product_requirements = request.POST.get('require')
            product_need = request.POST.get('need')
            product_do = request.POST.get('do')
            product_priority = request.POST.get('priority')

            OnBoardingPortal.new_product_name=product_name
            newproductname = OnBoardingPortal.new_product_name

            OnBoardingPortal.new_product+=1

            try:
                with open('./media/' + filename + '', "rb") as f:
                    encoded_string = base64.b64encode(f.read())

                    product_image = encoded_string.decode('utf-8')

                    def write_json(data, filename='test.json'):
                        with open(filename, 'w') as f:
                            json.dump(data, f, indent=4)

                    try:
                        with open('test.json') as json_file:
                            data = json.load(json_file)

                            temp = data


                            y = {
                                "id": "test",
                                "productName": product_name,
                                "shortDescription": product_description,
                                "imageUrl": product_image,
                                "productTerms": product_terms,
                                "productConditions": product_conditions,
                                "fullDescription": "None. ",
                                "productMinimumRequirements": product_requirements,
                                "productCode": product_code,
                                "applicableCurrencies": [product_currency

                                ],
                                "customFields": [{
                                    "hint": "Enter Your Full Address",
                                    "nameOfField": "address1",
                                    "fieldType": "STRING",
                                    "value": "null",
                                    "possibleValues": "null",
                                    "mandatory": "false"
                                }],
                                "conditions": product_conditions,
                                "whatYouNeed": [
                                    product_need
                                ],
                                "whatYouCanDo": [
                                    product_do
                                ],
                                "htmlPage": "None",
                                "priority": product_priority,
                                "lightKyc": product_kyc,
                                "deleted": "false"
                            }

                            # appending data to emp_details
                            temp.append(y)

                        write_json(data)

                        context = {'new_product_name': newproductname}
                        return render(request, 'accounts/success.html',context)
                    except:
                        print('Exception')
            except Exception as ex:
                print(ex, 'Occured')


        else:
            print('Failed')
    except Exception as ex:
        print('Exception ex')





    return render(request, 'accounts/product_add.html')

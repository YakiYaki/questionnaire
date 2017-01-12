from django.shortcuts import render

# Create your views here.

quiz_html = "quiz.html"

licenses = {'1': 'Business license',
            '2': 'Food handling and safety license',
            '3': 'Building license', '4': 'Liquor license',
            '5': 'Trademark license', '6': 'HAACP regulations',
            '7': 'VAT registration',
            '8': 'Insurance: property coverage, injuries coverage '
                 '(liability policies)',
            '9': 'Employee rules and regulations'}
cuisines = {'1': 'Pizzeria/Italian',
            '2': 'Asian',
            '3': 'Burgers/American',
            '4': 'Latin America',
            '5': 'Eastern',
            '6': 'German',
            '7': 'French',
            '8': 'Russian'}
targets = {'1': 'families',
           '2': 'businessmen',
           '3': 'students/youth',
           '4': 'couples',
           '5': 'tourists'}
things = {'1': 'Fire',
          '2': 'Water',
          '3': 'Ventilation',
          '4': 'Air conditioning',
          '5': 'Waste'}
trends = {'1': 'Storytelling experience',
          '2': 'Niche Targeting',
          '3': 'Celebrity Chef',
          '4': 'Latin America cuisine and culture',
          '5': 'Housemade products'}
pricing_tips = {'1': 'Cost-Plus Pricing = overhead costs + profit margin',
                '2': 'Consider "good, better, best" strategy',
                '3': 'Consider your target market for pricing',
                '4': 'Menu price = 130-135% of the actual food costs',
                '5': 'Vary the price ranges',
                '6': 'Place prices after the descriptions of the dishes',
                '7': 'Take out the price sign of the menu'}
supplier_tips = {'1': 'Make a detailed list of everything you need (equipment, furnishing, dinnerware, etc.)',
                 '2': 'Industry association can help in finding suppliers',
                 '3': 'Check legitimacy of a supplier'}
consider_points = {'1': 'Marketing plan',
                   '2': 'Social media: TripAdvisor, Yelp, Opentable, Facebook, Instagram',
                   '3': 'Advertising'}
social_media_platforms = {'1': 'TripAdvisor',
                          '2': 'Yelp',
                          '3': 'OpenTable',
                          '4': 'Facebook',
                          '5': 'Instagram',
                          '6': 'Google Reviews'}
line2 = False


def render_question(request, cap, next, type, add_cap="", input_cap="", vars=None, tip_cap="", tips=None,
                    add_inputs=None, icons=False, target=False, tip_type='text'):
    return render(request, quiz_html,
                  {'cap': cap, 'fn_next': next, 'add_cap': add_cap, 'type': type, 'vars': vars, 'tips': tips,
                   'tip_cap': tip_cap, 'add_inputs': add_inputs, 'input_cap': input_cap, 'icons': icons,
                   'target': target, 'tip_type': tip_type})


def quiz(request):
    if request.method == "GET" and 'fn' in request.GET:
        q_num = request.GET['fn']
        ans = request.GET['ans'] if 'ans' in request.GET else ""
        target = True if 'target' in request.GET else False

        if line2:
            if q_num == '3':
                return render_question(request, "Target market", 4, 'choice', vars=targets)
            elif q_num == '4':
                return render_question(request, "Location", 5, 'map')
            elif q_num == '5':
                return render_question(request, "Do you rent the place?", 6, 'yn')
            elif q_num == '6':
                if ans == 'yes':
                    return render_question(request, "What is the total monthly rent, including all the costs?", 7,
                                           'input',
                                           input_cap="euro",
                                           tip_cap='Please check the following before signing the contract',
                                           tips=things, tip_type='choice')
                else:
                    return render_question(request, "What is the usable surface area?", 8, 'input', input_cap="m2")
            elif q_num == '7':
                return render_question(request, "What is the usable surface area?", 8, 'input', input_cap="m2")
            elif q_num == '8':
                return render_question(request, "What is the usable surface area of the dining area?", 9, 'input',
                                       input_cap="m2")
            elif q_num == '9':
                return render_question(request, "How many seats do you have in the dining area?", 10, 'input',
                                       input_cap="seats")
            elif q_num == '10':
                return render_question(request, "Do you have a terrace?", 11, 'yn')
            elif q_num == '11':
                if ans == 'yes':
                    return render_question(request, "What is the usable surface area of the terrace?", 12, 'input',
                                           input_cap="m2")
                else:
                    return render_question(request, "Do you serve food at the bar?", 14, 'yn')
            elif q_num == '12':
                return render_question(request, "How many seats do you have on the terrace?", 13, 'input',
                                       input_cap="seats")
            elif q_num == '13':
                return render_question(request, "Do you serve food at the bar?", 14, 'yn')
            elif q_num == '14':
                return render_question(request, "How many seats do you have in total?", 15, 'input', input_cap="seats")
            elif q_num == '15':
                return render_question(request, "How many customers do you serve per day?", 16, 'input',
                                       input_cap="customers")
            elif q_num == '16':
                return render_question(request, "How many dishes do you serve per day?", 17, 'input',
                                       input_cap="dishes")
            elif q_num == '17':
                return render_question(request, "What is the Revenue?", 18, 'multi_input', input_cap="euro",
                                       add_inputs={'Food': '%', 'Beverage': '%'})
            elif q_num == '18':
                return render_question(request, "What are the total costs?", 19, 'multi_input', input_cap="euro",
                                       add_inputs={'Food': '%', 'Beverage': '%'})
            elif q_num == '19':
                return render_question(request, "What are your maintenance costs?", 20, 'input', input_cap="seats")
            elif q_num == '20':
                return render_question(request, "How many are there employees?", 21, 'multi_input', input_cap="employees",
                                       add_inputs={'Labour costs': '%'})
            elif q_num == '21':
                return render_question(request, "Do you do marketing?", 22, 'yn')
            elif q_num == '22':
                if ans == 'yes':
                    return render_question(request, "What are your marketing costs?", 23, 'input', input_cap="euro")
                else:
                    return render_question(request, "Do you have a financial reserve?", 24, 'yn')
            elif q_num == '23':
                return render_question(request, "Do you have a financial reserve?", 24, 'yn')
            elif q_num == '24':
                if ans == 'yes':
                    return render_question(request, "What is the amount of your reserve?", 25, 'input',
                                           input_cap="euro")
                else:
                    global line2
                    line2 = False
                    return render(request, 'done_quiz.html')
            elif q_num == '25':
                global line2
                line2 = False
                return render(request, 'done_quiz.html')

        if q_num == '1':
            if ans == 'no':
                return render_question(request, "Did you choose the cuisine type of your restaurant?", 2, 'yn')
            else:
                global line2
                line2 = True
                return render_question(request, "Cuisine type", 3, 'choice', vars=cuisines, target=True)
        elif q_num == '2':
            if ans == 'no':
                return render_question(request, 'Trends in Restaurant Industry for 2017', 2, 'tips', tips=trends)
            else:
                return render_question(request, "Cuisine type", 3, 'choice', vars=cuisines)
        elif q_num == '3' and not target:
            return render_question(request, "Did you choose where your restaurant will be located?", 4, 'yn')
        elif q_num == '3' and target:
            return render_question(request, "Target market", 28, 'choice', vars=targets)
        elif q_num == '4':
            if ans == 'yes':
                return render_question(request, "Location", 5, 'map')
            else:
                return render_question(request, "What is your target customer?", 28, 'choice', vars=targets)
        elif q_num == '5':
            return render_question(request, "Do you rent the place?", 6, 'yn')
        elif q_num == '6':
            if ans == 'yes':
                return render_question(request, "What is your monthly rent, including all the costs?", 7, 'input',
                                       input_cap="euro",
                                       tip_cap='Please check the following before signing the contract', tips=things,
                                       tip_type='choice')
            else:
                return render_question(request, "Contact local authorities!", 8, 'check', vars=licenses)
        elif q_num == '7':
            return render_question(request, "Contact local authorities!", 8, 'check', vars=licenses)
        elif q_num == '8':
            return render_question(request, "What is the usable surface area?", 9, 'input', input_cap="m2")
        elif q_num == '9':
            return render_question(request, "Do you have a terrace?", 10, 'yn')
        elif q_num == '10':
            if ans == 'yes':
                return render_question(request, "What is the usable surface area of the terrace?", 11, 'input',
                                       input_cap="m2")
            else:
                return render_question(request, "What is the usable surface area of the dining area?", 13, 'input',
                                       input_cap="m2")
        elif q_num == '11':
            return render_question(request, "How many seats do you have on the terrace?", 12, 'input',
                                   input_cap="seats")
        elif q_num == '12':
            return render_question(request, "What is the usable surface area of the dining area?", 13, 'input',
                                   input_cap="m2")
        elif q_num == '13':
            return render_question(request, "How many seats do you have in the dining area?", 14, 'input',
                                   input_cap="seats")
        elif q_num == '14':
            return render_question(request, "Do you serve food at the bar?", 15, 'yn')
        elif q_num == '15':
            # запомнить ответ вопроса 14: да или нет
            return render_question(request, "How many seats do you have in total?", 16, 'input', input_cap="seats")
        elif q_num == '16':
            return render_question(request, "What are your opening hours per week?", 17, 'input', input_cap="hours")
        elif q_num == '17':
            return render_question(request, "What is your average check?", 18, 'input', input_cap="euro",
                                   tip_cap='Pricing tips', tips=pricing_tips)
        elif q_num == '18':
            return render_question(request, "What are your total costs?", 19, 'multi_input', input_cap="euro",
                                   add_inputs={'Food': '%', 'Beverage': '%'})
        elif q_num == '19':
            return render_question(request, 'Supplier tips', 20, 'tips', tips=supplier_tips)
        elif q_num == '20':
            return render_question(request, "What is the number of employees in your restaurant?", 21, 'input',
                                   input_cap="employees", add_cap='Please, check the Employee Legal Handbook!')
        elif q_num == '21':
            return render_question(request, "Would you like to do marketing?", 22, 'yn')
        elif q_num == '22':
            if ans == 'no':
                return render_question(request, 'Points to consider', 23, 'tips', tips=consider_points)
            else:
                return render_question(request, "What are your marketing costs?", 24, 'input', input_cap="euro")
        elif q_num == '23':
            return render_question(request, "What are your marketing costs?", 24, 'input', input_cap="euro")
        elif q_num == '24':
            return render_question(request,
                                   "Will you register your restaurant on the following social media platforms?", 25,
                                   'check',
                                   vars=social_media_platforms, icons=True)
        elif q_num == '25':
            return render_question(request, "Do you have a financial reserve?", 26, 'yn')
        elif q_num == '26':
            if ans == 'yes':
                return render_question(request, "What is the amount of your reserve?", 27, 'input', input_cap="euro")
            else:
                return render(request, 'done_quiz.html')
        elif q_num == '27':
            return render(request, 'done_quiz.html')
        elif q_num == '28':
            return render_question(request, "Location", 5, 'map')
    else:
        return render_question(request, "Do you have a restaurant?", 1, 'yn')

    return render(request, 'quiz.html', {})


def index(request):
    global line2
    line2 = False
    return render(request, 'index.html')


def recs(request):
    return render(request, 'recs.html')


def contacts(request):
    return render(request, 'contacts.html')

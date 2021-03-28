from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from view.general import read_field

pricing_valuation_bp = Blueprint("pricing_valuation", __name__)

__pricing_valuation_data = []  # using a list instead of variable since it is mutable in a function


@pricing_valuation_bp.route("/pricing-valuation", methods=["GET", "POST"])
@login_required
def pricing_valuation():
    if request.method == "POST":
        ticker = read_field(("ticker-of-the-underlying-1", "ticker-of-the-underlying-111",
                             "ticker-of-the-underlying-121", "ticker-of-the-underlying-131"))
        expiration_date = read_field(("expiration-date1", "expiration-date17", "expiration-date113",
                                      "expiration-date119"))
        option_type = read_field(("option-type1", "option-type17", "option-type114", "option-type113"))
        option_style = read_field(("option-style1", "option-style17", "option-style113", "option-style141"))
        data_source = read_field(("data-source1", "data-source111", "data-source115", "data-source121"))
        itm_atm_otm = read_field(("itm-atm-otm1", "itm-atm-otm17", "itm-atm-otm116", "itm-atm-otm113"))

        # from control.controller import get_quantitative_analysis
        # analysis = get_quantitative_analysis(ticker, expiration_date, option_style, option_type, data_source,
        #                                      itm_atm_otm)
        #
        # if analysis is None:
        #     flash("Invalid ticker. Please try again", category="Error")
        # else:
        #     __pricing_valuation_data.insert(0, analysis)
        #     return redirect((url_for("pricing_valuation.pricing_valuation_result")))

        # # values for the input fields
        # from control.controller import get_expiration_date_list, get_option_type_list, get_option_style_list, get_data_source_list, get_itm_atm_otm_list
        # expiration_date_list = get_expiration_date_list()
        # option_type_list = get_option_type_list()
        # option_style_list = get_option_style_list()
        # data_source_list = get_data_source_list()
        # itm_atm_otm_list = get_itm_atm_otm_list()

    return render_template("pricing-and-valuation-page.html", user=current_user,
                           # field values
                           expiration_date1="1",
                           expiration_date2="2",
                           expiration_date3="3",
                           expiration_date4="4",
                           expiration_date5="5",
                           expiration_date6="6",
                           expiration_date7="7",
                           expiration_date8="8",
                           expiration_date9="9",
                           expiration_date10="10",
                           expiration_date11="11",
                           expiration_date12="12",
                           expiration_date13="13",
                           expiration_date14="14",
                           expiration_date15="15",
                           expiration_date16="16",

                           option_type1="1",
                           option_type2="2",

                           option_style1="1",
                           option_style2="2",

                           data_source1="1",
                           data_source2="2",

                           itm_atm_otm1="1",
                           itm_atm_otm2="2",
                           itm_atm_otm3="3",
                           itm_atm_otm4="4",
                           itm_atm_otm5="5"
                           )


@pricing_valuation_bp.route("/pricing-valuation/result", methods=["GET", "POST"])
@login_required
def pricing_valuation_result():
    # when the user entered tha page by pressing the analyze button
    if request.method == "POST":
        ticker = read_field(("ticker-of-the-underlying-17", "ticker-of-the-underlying-117",
                             "ticker-of-the-underlying-127", "ticker-of-the-underlying-137"))
        expiration_date = read_field(("expiration-date15", "expiration-date111", "expiration-date117",
                                      "expiration-date123"))
        option_type = read_field(("option-type15", "option-type111", "option-type132", "option-type117"))
        option_style = read_field(("option-style15", "option-style111", "option-style131", "option-style145"))
        data_source = read_field(("data-source17", "data-source117", "option-style133", "data-source127"))
        itm_atm_otm = read_field(("itm-atm-otm15", "itm-atm-otm111", "itm-atm-otm134", "itm-atm-otm117"))

    #     from control.controller import get_quantitative_analysis
    #     analysis = get_quantitative_analysis(ticker, expiration_date, option_style, option_type, data_source,
    #                                          itm_atm_otm)
    #
    #     if analysis is None:
    #         flash("Invalid ticker. Please try again", category="Error")
    #     else:
    #         __pricing_valuation_data.insert(0, analysis)
    #         return redirect((url_for("pricing_valuation.pricing_valuation_result")))
    #
    # # when the user entered the page without pressing the analyze button
    # try:
    #     analysis = __pricing_valuation_data[0]
    # except IndexError: # if this exception is thrown, it means the user refreshed the result page or entered by simply typing the url
    #     return redirect((url_for("pricing_valuation.pricing_valuation")))
    #
    # # clear the list so it doesn't grow as the user analyzes multiple times
    # __pricing_valuation_data.clear()
    #
    # # values for the input fields
    # from control.controller import get_expiration_date_list, get_option_type_list, get_option_style_list, get_data_source_list, get_itm_atm_otm_list
    # expiration_date_list = get_expiration_date_list()
    # option_type_list = get_option_type_list()
    # option_style_list = get_option_style_list()
    # data_source_list = get_data_source_list()
    # itm_atm_otm_list = get_itm_atm_otm_list()
    #
    # # analysis
    # variables = analysis["variables"]
    # valuations = analysis["valuations"]
    # the_greeks = analysis["the_greeks"]

    return render_template("pricing-and-valuation-page2.html", user=current_user,
                           # field values
                           expiration_date1="1",
                           expiration_date2="2",
                           expiration_date3="3",
                           expiration_date4="4",
                           expiration_date5="5",
                           expiration_date6="6",
                           expiration_date7="7",
                           expiration_date8="8",
                           expiration_date9="9",
                           expiration_date10="10",
                           expiration_date11="11",
                           expiration_date12="12",
                           expiration_date13="13",
                           expiration_date14="14",
                           expiration_date15="15",
                           expiration_date16="16",

                           option_type1="1",
                           option_type2="2",

                           option_style1="1",
                           option_style2="2",

                           data_source1="1",
                           data_source2="2",

                           itm_atm_otm1="1",
                           itm_atm_otm2="2",
                           itm_atm_otm3="3",
                           itm_atm_otm4="4",
                           itm_atm_otm5="5",

                           # # analysis values
                           # risk_free_rate=variables["risk_free_rate_r"],
                           # underlying_s=variables["underlying_s"],
                           # chosen_expiration=variables["chosen_expiration"],
                           # strike_x=variables["strike_x"],
                           # time_to_maturity_T=variables["time_to_maturity_T"],
                           # return_volatility=variables["return_volatility"],
                           # intrinsic_value=valuations["intrinsic_value"],
                           # speculative_premium=variables["speculative_premium"],
                           #
                           # black_scholes=valuations["black_scholes"],
                           # binomial=valuations["binomial"],
                           # average_price=valuations["average_price"],
                           # market_price=valuations["market_price"],
                           # implied_volatility=valuations["implied_volatility"],
                           #
                           # delta=the_greeks["delta"],
                           # gamma=the_greeks["gamma"],
                           # theta=the_greeks["theta"],
                           # vega=the_greeks["vega"],
                           # rho=the_greeks["rho"],
                           # charm=the_greeks["charm"]
                           )


@pricing_valuation_bp.route("/pricing-valuation/export")
@login_required
def pricing_valuation_export():
    return redirect(url_for("pricing_valuation.pricing_valuation"))

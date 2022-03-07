"""a Module to interact with Google PageSpeed Insights API"""
from urllib import request
import requests
import json

import urllib3


def ApiSpeed(website: str):
    """Test Website Performance

        Args:
            website: URL of WebSite to Test

        Returns:
            Print Website Performance.

        Example:
            ApiSpeed(URL)
    """
    url: str = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}&strategy=desktop&key=AIzaSyCcDNbRIvDPnuOM1TdCwoyzmP6NiGOkcLU".format(website)
    """API Request
        parameter:
            url: WebSite Link to Test
            strategy: testing environment either {mobile, desktop}
            key: API Key
    """

    response = requests.get(url)
    """Requesting Performance Evaluation"""

    data = json.loads(response.text)
    """Fetch JSON Response"""

    le_fcp = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
    """First Contentful Paint of loadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    le_fid = data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
    """First Input Delay of loadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    le_lcp = data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
    """Largest Contentful Paint of loadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    le_cls = data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
    """Cumulative Layout Shift Score of loadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    le_overall = data["loadingExperience"]["overall_category"]
    """Overall Performance of loadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """

    print("\n")
    print("loadingExperience:")
    print("First Contentful Paint: {}".format(le_fcp))
    print("First Input Delay: {}".format(le_fid))
    print("Largest Contentful Paint: {}".format(le_lcp))
    print("Cumulative Layout Shift Score: {}".format(le_cls))
    print("Overall Performance: {}".format(le_overall))
    print("")

    ole_fcp = data["originLoadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
    """First Contentful Paint of OriginLoadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    ole_fid = data["originLoadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
    """First Input Delay of OriginLoadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    ole_lcp = data["originLoadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
    """Largest Contentful Paint of OriginLoadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    ole_cls = data["originLoadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
    """Cumulative Layout Shift Score of OriginLoadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    ole_overall = data["originLoadingExperience"]["overall_category"]
    """Overall Performance of OriginLoadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """

    print("\n")
    print("originLoadingExperience:")
    print("First Contentful Paint: {}".format(ole_fcp))
    print("First Input Delay: {}".format(ole_fid))
    print("Largest Contentful Paint: {}".format(ole_lcp))
    print("Cumulative Layout Shift Score: {}".format(ole_cls))
    print("Overall Performance: {}".format(ole_overall))
    print("")

    lh_fcp = data["lighthouseResult"]["audits"]["first-contentful-paint"]["displayValue"]
    """First Contentful Paint of lighthouseResult
        :returns: in Seconds.
    """
    lh_tti = data["lighthouseResult"]["audits"]["interactive"]["displayValue"]
    """Time to Interactive of lighthouseResult
        :returns: in Seconds.
    """
    lh_lcp = data["lighthouseResult"]["audits"]["largest-contentful-paint"]["displayValue"]
    """Largest Contentful Paint of lighthouseResult
        :returns: in Seconds.
    """
    lh_cls = data["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"]
    """Cumulative Layout Shift Score of lighthouseResult
        :returns: in Seconds.
    """
    lh_tbt = data["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"]
    """Total Blocking Time of lighthouseResult
        :returns: in Seconds.
    """
    lh_si = data["lighthouseResult"]["audits"]["speed-index"]["displayValue"]
    """Speed Index of lighthouseResult
        :returns: in Seconds.
    """
    for i in lh_fcp:
        if i == " " or i == "s" or i == "ms"or i == "m":
            lh_fcp =lh_fcp.replace(i,"")

    
    for i in lh_tti:
        if i == " " or i == "s" or i == "ms"or i == "m":
            lh_tti =lh_tti.replace(i,"")

    
    for i in lh_lcp:
        if i == " " or i == "s" or i == "ms"or i == "m":
            lh_lcp =lh_lcp.replace(i,"")

    
    for i in lh_cls:
        if i == " " or i == "s" or i == "ms"or i == "m":
            lh_cls =lh_cls.replace(i,"")

    
    for i in lh_tbt:
        if i == " " or i == "s" or i == "ms"or i == "m":
            lh_tbt =lh_tbt.replace(i,"")

    
    for i in lh_si:
        if i == " " or i == "s" or i == "ms" or i == "m":
            lh_si =lh_si.replace(i,"")            

    print("\n")
    print("lighthouseResult:")
    print("First Contentful Paint: {}".format(lh_fcp))
    print("Time to Interactive: {}".format(lh_tti))
    print("Largest Contentful Paint: {}".format(lh_lcp))
    print("Cumulative Layout Shift Score: {}".format(lh_cls))
    print("Total Blocking Time: {}".format(lh_tbt))
    print("Speed Index: {}".format(lh_si))
    print("")

    overall_performance = data["lighthouseResult"]["categories"]["performance"]["score"] * 100
    """Overall Performance of lighthouseResult
        :returns: performances: in Percentage.
    """
    print("Overall Performance: {}".format(overall_performance))
    print("")
    
    urlPost = "https://a5r-testing.herokuapp.com/createNewtestSpeed"
    data = {
        "loadingExperince":le_overall,
        "LE_FCP":le_fcp,
        "LE_FID":le_fid,
        "LE_CLS":le_cls,
        "LE_LCP":le_lcp,
        "OriginLoadingExperince":ole_overall,
        "OLE_FCP":ole_fcp,
        "OLE_FID":ole_fid,
        "OLE_CLS":ole_cls,
        "OLE_LCP":ole_lcp,
        "LH_TBT":lh_tbt,
        "LH_SI":lh_si,
        "LH_FCP":lh_fcp,
        "LH_TTI=":lh_tti,
        "LH_CLS":lh_cls,
        "LH_LCP":lh_lcp,
        "PR_Precentage":overall_performance
    }
    
    requests.post(url = urlPost , json=data , headers= { "Content-Type": "application/json" })
    """
    post_url = "https://a5r-testing.herokuapp.com/createNewtestSpeed"

    #print(len(data)-1)
    #print(len(data['get']))

    data = {
        
    "loadingExperince": "ok",
    "LE_FCP": "ok",
    "LE_FID": "ok",
    "LE_CLS": "ok",
    "LE_LCP": "ok",
    "OriginLoadingExperince": "ok",
    "OLE_FCP": "ok",
    "OLE_FID": "ok",
    "OLE_CLS": "ok",
    "OLE_LCP": "ok",
    "LH_TBT": "1",
    "LH_SI": "1",
    "LH_FCP": "1",
    "LH_TTI": "1",
    "LH_CLS": "1",
    "LH_LCP": "1",
    "PR_Precentage": 1.5
    }
    requests.post(url=post_url, json=data, headers={'Content-Type': 'application/json'})"""
    


if __name__ == "__main__":
    ApiSpeed("https://facebook.com")


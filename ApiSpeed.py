"""Making a request to get data from PageSpeed Insights API using urllib.request"""
import urllib.request
import json

def ApiSpeed(website:str):
  """urllib.request module and make a requests to this URL
  url =https://www.googleapis.com/pagespeedonline/v5/runPagespeed? url={}& strategy=desktop or mobile &key =api key. format(website)"""

  url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}&strategy=desktop&key=AIzaSyCcDNbRIvDPnuOM1TdCwoyzmP6NiGOkcLU".format(website)

  """Extension library to opening urls"""
  response = urllib.request.urlopen(url)

  """storing the JSON response from url in data"""
  data = json.loads(response.read())

  """To get we are searching for the Loading Experience key and select the category for each metric
    It will return FOUR type of performances: “Slow“, “Average”, “None” and “Fast“.  
  """
  fcp = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
  fid = data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
  lcp = data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
  cls = data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
  overall = data["loadingExperience"]["overall_category"]
  print("loadingExperience:")
  print("FIRST_CONTENTFUL_PAINT_MS :",fcp)
  print("FIRST_INPUT_DELAY_MS :" ,fid)
  print("LARGEST_CONTENTFUL_PAINT_MS:" ,lcp)
  print("CUMULATIVE_LAYOUT_SHIFT_SCORE:" ,cls)
  print("OVERALL_CATEGORY:" ,overall)

  """To get we are searching for the  Origin Loading Experience key and select the category for each metric
    It will return FOUR type of performances: “Slow“, “Average”, “None” and “Fast“.  
  """
  fcp = data["originLoadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
  fid = data["originLoadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
  lcp = data["originLoadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
  cls = data["originLoadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
  overall = data["originLoadingExperience"]["overall_category"]
  
  print("originLoadingExperience:")
  print("FIRST_CONTENTFUL_PAINT_MS :" ,fcp)
  print("FIRST_INPUT_DELAY_MS :" ,fid)
  print("LARGEST_CONTENTFUL_PAINT_MS:" ,lcp)
  print("CUMULATIVE_LAYOUT_SHIFT_SCORE:" ,cls)
  print("OVERALL_CATEGORY:" ,overall)


  """To get we are searching for the Light house key and select the category for each metric
    It will return  type of performances:  “Seconds“.  
  """
  fcp = data["lighthouseResult"]["audits"]["first-contentful-paint"]["displayValue"]
  tto = data["lighthouseResult"]["audits"]["interactive"]["displayValue"]
  lcp = data["lighthouseResult"]["audits"]["largest-contentful-paint"]["displayValue"]
  cls = data["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"]
  tbt = data["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"]
  si  = data["lighthouseResult"]["audits"]["speed-index"]["displayValue"]

  print("lighthouseResult:")
  print("FIRST_CONTENTFUL_PAINT :" ,fcp)
  print("TIME_TO_INTERACTIVE :" ,tto)
  print("LARGEST_CONTENTFUL_PAINT :" ,lcp)
  print("CUMULATIVE_LAYOUT_SHIFT :" ,cls)
  print("TOTAL_BLOCKING_TIME :" ,tbt)
  print("SPEED_INDEX :" ,si)

  """Overall for light house performance ,it will return a percentage
  """
  overall_performance = data["lighthouseResult"]["categories"]["performance"]["score"] * 100
  print("PEFORMANCE :" ,overall_performance)
  

if __name__=="__main__":
 ApiSpeed("https://facebook.com")  

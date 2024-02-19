# download data and save as csv

import requests

data = 'Data'
urls = {
  'cpu': ['https://www.cpubenchmark.net/CPU_mega_page.html'],
  'gpu': ['https://www.videocardbenchmark.net/GPU_mega_page.html'],
  'hdd': ['https://www.harddrivebenchmark.net/hdd-mega-page.html'],
  'ram': ['https://www.memorybenchmark.net/ram_list.php',  
          'https://www.memorybenchmark.net/ram_list-ddr4.php',  
          'https://www.memorybenchmark.net/ram_list-ddr3.php']
}

for device, address_list in urls.items():
  for address  in address_list:
    res = requests.get(address)
    if res.status_code != 200:
      raise requests.ConnectionError(address)

    
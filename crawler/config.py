# -*- coding: utf-8 -*-

# ---------------------------
# 用户配置
# ---------------------------
DOWNLOAD_DIR       = 'downloads'
DOIS_FILE          = 'dois.txt'
UNPAYWALL_EMAIL    = "1085503167@qq.com"   # 用你自己的邮箱
UNPAYWALL_URL      = "https://api.unpaywall.org/v2/{doi}?email={email}"
Europe_PMC_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{doi}&resultType=core&format=json"
Open_Access_Button_URL = "https://bg.api.oa.works/find?id={doi}"
SCIENCE_DIRECT_URL = "https://api.elsevier.com/content/article/doi/{doi}?view=FULL"
SCIENCE_DIRECT_X_ELS_APIKey = "12a8eb40c97addbf7e1aa5ac939c7bdb"
CROSSREF_URL = "https://api.crossref.org/works/{doi}"


# 不可用的api
# SPRINGER_NATURE_API_KEY = "88d2ae1c43e22c7c399ed51c87be3272"
# SPRINGER_NATURE_URL = "https://api.springernature.com/openaccess/jats"
# WILEY_URL = "https://onlinelibrary.wiley.com/doi/pdf/{doi}"
# CHEMISTRY_EUROPE = "https://chemistry-europe.onlinelibrary.wiley.com/doi/epdf/{doi}"


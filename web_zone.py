import os 


css_media_query="""
@media (min-width:1440px) {}

@media (min-width:1025px) and (max-width:1439px) {}

@media (min-width:901px) and (max-width:1024px) {}

@media (min-width:601px) and (max-width:900px) {}

@media (max-width:600px) {}
"""

html_page_structure="""

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>
<header>
    <h1>Player</h1>
</header>

<body>
    <section id="c1"></section>
    <section id="c2"></section>
    <section id="c3">
    
    <div onLoad='call_now();'></div>
    </section>
    <script src="js_1.js"></script>
</body>
<footer>
    <h4>footer</h4>
</footer>

</html>

"""




JS_CONTENT_MODEL="""

function call_now(){
      for(int i=0;i<10;i++){
            return"<h1>call 911</h1>"
      }
}

"""






folder_in=input("enter the folder name:")

while True:
      act_1=os.mkdir(folder_in)
      act_1=os.system("nul>"+folder_in+"/page.html")
      wr=open(folder_in+"/page.html","+w")
      wr.write(html_page_structure)
      wr.close()
      act_1=os.system("nul>"+folder_in+"/style.css")
      wr=open(folder_in+"/style.css","+w")
      wr.write(css_media_query)
      wr.close()
      act_1=os.system("nul>"+folder_in+"/js_1.js")
      wr=open(folder_in+"/js_1.js","+w")
      wr.write(JS_CONTENT_MODEL)
      wr.close()
      #if folder_in == "xxx":exit()




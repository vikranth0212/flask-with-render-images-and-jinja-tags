from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/send_html')
def send_html():
    return render_template('send_html.html',name='vicky')

@FAI.route('/properties')
def properties():
    return render_template('properties.html')
    
if __name__=='__main__':
    FAI.run(debug=True)    


#in flask we need to give proper names for folder
# for html pages we need to give 'templates' only
#and keeping all the images,css,js files in 'static' folder
#for writing urls.py,manage.py and for views we need to create a file not a folder in project
#in flask we cannot create project,here we are creating a folder which will act as container
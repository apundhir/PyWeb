'''
Created on Jan 28, 2013

@author: Ajay Pratap Singh Pundhir
'''
import webapp2

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
form = '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="ISO-8859-1">
            <title>Ajay Pratap Singh Pundhir</title>
        </head>
        <body>
            What is your DOB???
            <br>
            <form method="post">
                <label>Day
                    <input type="text" name="Day" value="%(Day)s">
                </label>
                <label>Month
                    <input type="text" name="Month" value="%(Month)s">
                </label>
                <label>Year
                    <input type="text" name="Year" value="%(Year)s">
                </label>
                <br>
                <div Style="color: red">%(error)s</div>
                <br>
                <input type="submit">
            </form>
        </body>
        </html>
        '''

def valid_month(month):
    if month:
        cap_month = month.capitalize()
        if cap_month in months:
            return cap_month

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day
        
def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if int(year) >= 1900 and int(year) <= 2020:
            return int(year)

def escape_html(s):
    for (i,o) in (("&", "&amp;"), (">", "&gt;"), ("<", "&lt;"), ('"', "&quot;")):
        s = s.replace(i,o)
    return s             

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", day="", month="", year=""):
        return form % {"error": error,
                       "Day": escape_html(day),
                       "Month": escape_html(month),
                       "Year": escape_html(year)}
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(self.write_form())
    def post(self):
        user_day = self.request.get('Day')
        user_month = self.request.get('Month')
        user_year = self.request.get('Year')
        
        day = valid_day(user_day)
        month = valid_month(user_month)
        year = valid_year(user_year)
        
        if not (day and month and year):
            self.response.out.write(self.write_form("This does not seems to be the correct values!!", user_day, user_month, user_year))
        else:    
            self.redirect("/thanks")
            
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks!!, That is accepted date.")
        
        
        
app = webapp2.WSGIApplication([('/', MainPage),('/thanks', ThanksHandler)], debug=True)

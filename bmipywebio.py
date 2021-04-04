from pywebio.input import *
from pywebio.output import *
from pywebio.session import *



def bmicalculator():
    height=input("Please enter the height in cm",type=FLOAT)
    weight=input("Please enter the weight in Kg",type=FLOAT)
    
    bmi=weight/(height/100)**2
    
    bmi_output=[(16, 'severely underweight'), (18.5, 'underweight'),
                  (25, 'normal'), (30, 'overweight'),
                  (35, 'moderately obese'), (float('inf'), 'severely obese')]
    
    for tuple1,tuple2 in bmi_output:
        if bmi<=tuple1:
            put_text('BMI Standard Chart : ')
            put_table([
            {"BMI":"Below 16", "Category": "Extremely Underweight"},
            {"BMI":"Between 16 and 18.5", "Category": "Underweight"},
            {"BMI":"Between 18.5 and 25", "Category": "Normal"},
            {"BMI":"Between 25 and 30", "Category": "Overweight"},
            {"BMI":"Between 30 and 35", "Category": "Moderately Obese"},
            {"BMI":"Above 35", "Category": "Extremely Obese"}], header=["BMI", "Category"]) 

            put_markdown('**Your Body Mass Index (BMI) is %.1f and you are considered to be %s.**'%(bmi,tuple2))


            put_image('https://lh3.googleusercontent.com/-5jrhgbC0HjE/TYYaN-bViDI/AAAAAAAABlE/R-LsEooyzx0/s1600/Thanks2.png')
            
            break
    
if __name__=='__main__':
    bmicalculator()

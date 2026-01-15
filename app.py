from flask import Flask,render_template,request
from time import time
import random as rd

app=Flask(__name__)
sentences=["The democratic process relies heavily on the participation of citizens who actively engage in voting, ensuring that government officials are held accountable to the people they serve while maintaining a fair and transparent electoral system.",
           "Global leaders must collaborate to address critical challenges such as climate change, economic inequality, and geopolitical tensions in order to foster peace and sustainable development for future generations.",
           "In the world of professional basketball, athletes train rigorously to hone their skills, with each player focusing on improving their shooting accuracy, ball handling, and defensive strategies to contribute to their team's success.",
           "The industrial revolution marked a pivotal moment in human history, leading to unprecedented technological advancements, transforming societies from agrarian economies to urbanized industrial powerhouses with profound effects on labor and social structures.",
           "The excitement of the World Cup draws millions of fans from across the globe, all eager to witness their national teams compete for the prestigious trophy while celebrating the sport's unifying power.",
           "Ancient civilizations, such as the Egyptians, Greeks, and Romans, made lasting contributions to art, philosophy, science, and architecture, laying the foundation for much of modern Western culture and thought.",
           "Shakespeare's plays, with their intricate characters, timeless themes, and masterful use of language, continue to captivate audiences worldwide, offering profound insights into human nature, power dynamics, and the complexities of love and betrayal.",
           "The exploration of outer space has captivated humanity for centuries, and with missions to Mars, the search for extraterrestrial life, and the development of new space technologies, we are on the verge of expanding our understanding of the universe.",
           "The novel '1984' by George Orwell serves as a chilling warning about the dangers of totalitarianism, government surveillance, and the erosion of individual freedoms, providing a stark vision of a dystopian society under constant control.",
           "Inflation and unemployment rates are key indicators that policymakers monitor closely in order to maintain economic stability, while central banks adjust interest rates to influence consumer spending, investment, and overall economic activity.",
           "Climate change poses one of the greatest threats to our planet, with rising global temperatures, sea level rise, and extreme weather events leading to the loss of biodiversity and affecting millions of people who depend on natural resources for survival.",
           "Conservation efforts to protect endangered species, restore ecosystems, and reduce pollution are critical in preserving the planet's biodiversity and ensuring that future generations can enjoy the beauty and benefits of nature.",
           "The James Webb Space Telescope, launched in 2021, is poised to revolutionize our understanding of the cosmos, providing unprecedented images of distant galaxies, exoplanets, and the formation of stars, as well as giving scientists a deeper insight into the origins of the universe.",
           "Inflation and unemployment rates are key indicators that policymakers monitor closely in order to maintain economic stability, while central banks adjust interest rates to influence consumer spending, investment, and overall economic activity."]
def mistake(userinput,compinput):
    error=0
    user_words=userinput.strip()
    comp_words=compinput.strip()
    for i in range(min(len(user_words),len(comp_words))):
            if user_words[i]!=comp_words[i]:
                error+=1
            else:
                 continue
    error+=abs(len(user_words)-len(comp_words))
    return error

def calculateTime(startTime,endTime,userInput):
    total_time=(endTime-startTime)/60
    words=len(userInput)/5/total_time
    return round(words)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        sentence=request.form['typing-paragraph']
        start_time=float(request.form['start-time'])
        user_typed=request.form['user-input']
        end_time=time()
        total_time=round((end_time-start_time)/60)
        errors=mistake(user_typed,sentence)
        wpm=calculateTime(start_time,end_time,user_typed)
        return render_template('result.html',sentence=sentence,total_time=total_time,errors=errors,wpm=wpm)
    sentence=rd.choice(sentences)
    start_time=time()
    return render_template('index.html',sentence=sentence,start_time=start_time)   
if __name__=='__main__':
    app.run(debug=True)
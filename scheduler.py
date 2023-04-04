import time
import random



biblequotes = [
    ["1 Corinthians 15:58 : Therefore, my beloved brethren, be steadfast, immovable, always abounding in the work of the Lord, knowing that your labor is not in vain in the Lord. " ],
    ["Galatians 1:10: For do I now persuade humans, or God? Or do I seek to please humans? For if I still pleased men, I would not be a bondservant of Christ."],
    ["James 5:16 : Confess your trespasses to one another, and pray for one another, that you may be healed. The effective, fervent prayer of a righteous man avails much. "],
    ["Joshua 1:9Strong and Courageous - Joshua 1:99 Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the LORD your God will be with you wherever you go."],
    ["Psalms 118:6-8 The Lord is on my side;I will not fear. What can man do to me? The Lord is for me among those who help me;Therefore I shall see my desire on those who hate me. It is better to trust in the LordThan to put confidence in man."]
]
hinduquotes = [
    ["The human body is the temple of God. One who kindles the light of awareness within gets true light.The sacred flame of your inner shrineis constantly bright. The experience of unityis the fulfillment of human endeavors. The mysteries of life are revealed. (Rig Veda)"],
    ["O Brahma, lead us from the unreal to the real. O Brahma, lead us from darkness to light. O Brahma, lead us from death to immortality. Shanti, Shanti, Shanti, Om.(Brhadaranyaka Upanishad)"],
    ["In order to carry a positive action we must develop here a positive vision. (Dalai Lama)"],
    ["When you are discontent, you always want more, more, more. Your desire can never be satisfied. But when you practice contentment, you can say to yourself, 'Oh yes - I already have everything that I really need.'(Dalai Lama)"],
    [" In the practice of tolerance, one's enemy is the best teacher. (Dalai Lama) "]

]

h = hinduquotes
b = biblequotes
quotes = [h,b]
class Main:
 def __init__(self, name):
     main = Main
     self.name = name


 def quoteoftheday(self):
        while True:
            print("-----------------------------------------------------------------")
            print("B = Bible Quotes: H= Buddhist,Hindu,Tibetan quotes R = Random Quote")
            print("-----------------------------------------------------------------")
            quote_type = (input("What quote are you feeling?  " + str(self.name) + " ?? :").upper())
            if quote_type == "B" or "H" or "R" and quote_type.isalpha() :
                quote = self.randomizequote(quote_type)
                print(self.read(quote_type))
                if quote == None:
                    print("Please type something that works")
                else:
                    print(", ".join(quote))
                    time.sleep(100)
                    print(" Once you've wen ahead and done that be sure to meditate for 10 minutes, go on youtube and put calming music if you need to!")
                    print("feeling good")
                    break


 def randomizequote(self,quote_type):
    for input in quote_type:
        if quote_type == "B" :
            for quote in b:
                quote = random.choice(b)
                return quote
        elif quote_type == "H":
            for quote in h:
                quote= random.choice(h)
                return quote
        elif quote_type == "R":
            quotes = b + h
            for quote in quotes:
                quote= random.choice(quotes)
                return quote
 def read(self,quote_type):
    for input in quote_type:
        if quote_type == "B" :
            quote = "Please read this part in the bible!"
            return quote
        elif quote_type == "H":
            quote = "Please read the Bhuddism Guide!"
            return quote

#Make a main menu screen that ask you what you want to do



#


main = Main("Jayfec")
main.quoteoftheday()
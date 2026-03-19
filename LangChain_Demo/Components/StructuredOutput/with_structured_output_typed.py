from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from typing import TypedDict, Annotated, Optional, Literal

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(repo_id='meta-llama/Llama-3.3-70B-Instruct')

model = ChatHuggingFace(llm=llm)


# Define the output schema using TypedDict
class ReviewSummary(TypedDict):
    Summary : Annotated[str, "Write a concise summary of the review in 2-3 sentences."]
    sentiment: Annotated[Literal['Positive, Negative, or Neutral.'], "Determine the overall sentiment of the review"]
    pros: Annotated[Optional[list[str]], "List the positive aspects mentioned in the review."]
    cons: Annotated[Optional[list[str]], "List the negative aspects mentioned in the review."]

review = """
I bought the 1.5 ton 3 star 2025 model in the month of Feb '25 and am writing this review after using it for a few hours every night since 3 weeks. In Bengaluru, it's not yet the summer peak but it gets hot during the day ~31 deg.

I’m only going to talk about issues because the performance of the AC is top notch.

1. As soon as the AC arrived for delivery, I checked to make sure it was manufactured in 2025 before asking them to bring it upstairs to my house. After the delivery, I noticed the IDU carton has serial numbers for both the IDU (in-door unit) and ODU (out-door unit) printed outside. Apparently, they are a matching set, so Carrier has mentioned both serial numbers in the IDU box. This is where the first issue began. When I checked the ODU carton, I saw the serial number did not match with the IDU box. I checked the invoice, and the ODU serial no. mentioned there was the not matching with the ODU I received. So, I called up Amazon customer care and reported the issue and they confirmed that in the future if any issue arises with the AC, the technicians will check the invoice first. If the serial numbers don't match, they will reject the warranty. Amazon asked me to return the item but first the AC technicians who come for installation must give me a job sheet saying the ODU is different from the one mentioned in the invoice. That job sheet will be checked by the Amazon people coming for the return pick up. Next day when the technicians arrived, they said it doesn't matter if the ODU is a different one as long as the model no.s are the same. They convinced me after installation they have the authority to put in the new ODU serial number into the system and activate the warranty on that serial no. I asked them repeatedly if they are sure, and they said they do it all the time. This goes to show the seller doesn't bother to match the correct IDU and ODU while shipping these products. He just sends both of them randomly but ensures they are the same model and make. So don't bother much about the serial no.s on the IDU box matching with the ODU. They installed the AC, updated the new ODU on their app and asked me to download the 'Cool Connect' app to double check. Surely enough, when I logged in with my phone number, I saw the model number and new serial number of my AC updated along with the warranty details.

2. The technicians will try and sell you all kinds of stuff. First, they try to convince you to buy a stabilizer, although the company advertises an inbuilt one. I told them I will take the risk, and moreover they can’t turn down a repair because the company itself says 'stabilizer free operation'. Then comes the extra drainpipe which costs Rs 300 for 3 meters. I needed 8 meters which I bought in advance from the local HW shop for a total of Rs 400. Ask for the small size washing machine inlet pipe, it's the same thing. Next was the AC stand which cost Rs 999. I had already bought a very good quality one from Flipkart for Rs 499. Looking at that, they said they levy a Rs 300 installation charge if you don't buy from them. I didn't have a problem with that, but I think you can buy the one they bring along if it’s of good quality since you're just saving Rs 200. Then the 3-pin plug which from them would cost Rs 120, outside its half that. They will make all kinds of excuses when you ask them for a vacuum pump. I didn't care since no one used these pumps before and we've had ACs in our houses for the past 15 years. Vacuum pumps are generally used when you relocate because that's when air gets into the pipes. These come factory sealed.

3. That night when I ran the AC for an hour, I realised the IDU was leaking water inside the house. The technicians didn’t bother to check if the drainpipe was connected to the IDU correctly. This must be done by removing the outer cover of the IDU. I got to know this at night, so I called them the next day. They came back on the third day and connected the drainpipe to the internal outlet after removing the IDU cover. Now the water drains outwards and goes through the drainpipe.

4. The same night, I also noticed the ODU making a strange rattling sound. See the video attached. It was more prominent at night because everything was quieter. I had my suspicions after the technicians left in the afternoon, but wasn't sure because there's a house construction on the adjacent road with a lot of noise. At nighttime, I could easily make out there was an issue. After a bit of investigation, I found the grill that covers the fan is slightly loose and is vibrating when the ODU turns on, causing the rattling noise. I checked the following day and night as well and on the third day I lodged a complaint with customer care. Another technician showed up the following day and confirmed there is an issue. He also said the grill is loose and needs to be replaced, for which he raised a ticket and asked me to wait for 3 days for the spares to arrive. After about 10 days and 2 follow ups he arrived with the spare. Instead of just the grill he brought the entire backside frame with the grill attached. But when he unpacked the box, we saw the spare frame didn’t have the Carrier logo on it. So, I asked him to replace just the grill from that frame. That's when we noticed the new grill (circular in shape) had 4 screws to fasten it to the frame but the one on my ODU had only 2 screws (top and bottom) which was the reason why it was loose. When we replaced it with the spare grill and put in all 4 screws in the N-S- E-W direction, the rattling noise disappeared immediately. This tells us these ACs arrive in pieces and are assembled here at the warehouse, which is why they might have put some other model's grill on mine.

Now with all these issues resolved, I am a happy man.

Beware of the technicians forcing you to rate them on the ‘Cool Connect’ app. They lie to you by saying they need to take a pic of your rating which is not true. I realised this after I gave them 5 stars. Now I want to change it back to 3 stars but there’s no option for that. Tell them you will rate them after checking the performance of the AC for a few days and checking out things like leakages, if any.

I saw a few reviews that say the IDU is very silent. This is not entirely true. The fan speed, even at its minimum setting, is easily noticeable by anyone who walks into the room. Because of this, the air flow is higher and if you're sleeping in front of it, you are definitely going to feel cold very soon. Although not silent, it is tolerable and eventually in a few days, you'll get used to it. Unfortunately, I can’t compare it to any other AC in my house because all others are 1 ton each and are so silent, you wouldn't even know they are switched on. I'm guessing 1.5-ton 3-star ACs might probably make a little more noise than the 1 tons’. But now that I'm used to it, I don't have a problem.
The AC does not remember any swing settings. Whenever you turn it on, it will always start with the same swing flap position every time which is half down, regardless of whether you switched it off with the swing function on or at a certain angle. This is a bit irritating for me because every time I switch it on, I have to press another button for activating the swing every time. If I keep the swing flap at a certain position and switch off the AC, it goes back to a default position when I switch on the AC again. So you have to set the swing flap to your desired position every time.

All the other features like Flexi-Cool are bogus. They are just different settings of the fan speed and temperature with a fancy name. Also, I don’t think either of the Fexi-Cool options are working for me except the FC6 one. I tried them and nothing happened. The FC6 (Insta Cool) worked. I don’t really care because I always keep the AC in the lowest fan speed with 24-26 as the temp. This way it uses about 0.5 units per hour of electricity after the room reaches the set temperature. In the remote, the central buttons like power, mode, fan, temp control glow in the dark. It comes with backlight as well. It looks good enough to me. Not sure what expectations other people have for which they say it looks cheap. To me its good enough. The IDU has that LED strip light which you can see in their ads. This model does not have LEDs attached. So it will not turn on. That one in the ads is the Lumo model, I think. It’s a useless feature for me because the temp display is bright enough to use as a night light if you want to.

I like this AC and will definitely recommend going for it. Carrier is a well-established brand that goes back several decades and with the issues I faced, I am convinced that here in Bengaluru at least they have a good service center and they respond to complaints promptly.

"""

structured_model = model.with_structured_output(ReviewSummary)

result = structured_model.invoke(review)
print(result['sentiment'])





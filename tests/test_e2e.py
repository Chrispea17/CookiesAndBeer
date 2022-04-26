#The reason I created this end to end test spot was to actually figure out if I had made the domain model work so basically I do follow the input of the initail point of user gets recommendations to the endpoint of a ranked list of users. I was getting stuck on what do I need next so I think this provides a base for a what I am missing in th model

#Step one(implicit) User asks for a request for friends to recommend an item type. These requests are implicit for now and "taken care of in the UI"
# Step two(explicit): recommendations are stored and available for review 
#Step 3: the requester then chooses a recommendation to try it out 
#Step 4: The User rates the recommendation 1 or 0
#Step 5: User to User ranking is calculated and 
#Setp 6: All recommenders for that requester are listed in the interface by their ranking and the next time a new request is made thee ranking shows the recommendations of the top recommenders first.

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    itemID: str #for now, I'm not sure why this wouldn't end up being an iterated iteger?
    itemName: str



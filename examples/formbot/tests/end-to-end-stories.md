## Happy path
* greet: hi
    - utter_greet
* request_restaurant: im looking for a restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou: thanks
    - utter_noworries

## Happy path with message providing requested value
* greet: hi
    - utter_greet
* request_restaurant: im looking for a restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* inform: [afghan](cuisine) food
    - restaurant_form
    - form{"name": null}
    - utter_slots_values
* thankyou: thanks
    - utter_noworries
 
## unhappy path
* greet: hi
    - utter_greet
* request_restaurant: im looking for a restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* chitchat: can you share your boss with me?
    - utter_chitchat
    - restaurant_form
    - form{"name": null}
    - utter_slots_values
* thankyou: thanks
    - utter_noworries
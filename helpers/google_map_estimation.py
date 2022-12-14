import googlemaps


class Estimation:
    def __init__(self):
        self._gmaps = googlemaps.Client(
            key="AIzaSyBHc8BNV_qT0up1uO0oysWlLa876xLysqw")

    def evaluate(self, location, des_geo, destination_id):
        cal_dis = self._gmaps.distance_matrix(
            location, destinations=des_geo, mode='walking')
        if location == des_geo:
            cost = 0
        else:
            cost = cal_dis['rows'][0]['elements'][0]['duration']['text']
        guide_url = 'https://www.google.com/maps/dir/?api=1&origin={},{}&destination={},{}&destination_place_id={}8&travelmode={}'.format(
            location[0], location[1], des_geo[0], des_geo[1], destination_id, 'walking')
        return cost, guide_url

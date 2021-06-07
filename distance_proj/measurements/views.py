from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from .forms import MeasurementModelForm
from .models import Measurements
from .utils import get_geo, get_center_cordinates, get_zoom,get_ip_address
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium


class CalculateView(CreateView):
    template_name = 'measurements/main.html'
    form_class = MeasurementModelForm
    context_object_name = "form"
    # success_url = 'measurements:calculate_view'
    destination = None
    distance = None
    geolocator = Nominatim(user_agent='measurements')
    ip = '72.14.207.99'
    country, city, lat, lon = get_geo(ip)
    location = geolocator.geocode(city)
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)
    m = folium.Map(width=800, height=500, location=get_center_cordinates(l_lat, l_lon), zoom_start=8)
    folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                  icon=folium.Icon(color='purple')).add_to(m)

    # m = m._repr_html_()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map'] = self.m._repr_html_()
        try:
        # if Measurements.objects.filter(pk=self.kwargs['pk']).exists:
            context['distance'] = Measurements.objects.get(pk=self.kwargs['pk']).distance
            context['destination'] = self.geolocator.geocode(Measurements.objects.get(pk=self.kwargs['pk']).destination)
        # else:
        except KeyError:
            context['distance'] = self.destination
            context['destination'] =self.distance
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        destination_ = form.cleaned_data['destination']
        destination = self.geolocator.geocode(destination_)
        d_lat = destination.latitude  # широта
        d_long = destination.longitude  # долгота
        pointB = (d_lat, d_long)
        distance = round(geodesic(self.pointA, pointB).km, 2)

        CalculateView.m = folium.Map(width=800, height=500,
                                     location=get_center_cordinates(self.l_lat, self.l_lon, d_lat, d_long),
                                     zoom_start=get_zoom(distance))
        folium.Marker([d_lat, d_long], tooltip='click here for more', popup=destination,
                      icon=folium.Icon(color='red', icon='cloud')).add_to(self.m)
        folium.Marker([self.l_lat, self.l_lon], tooltip='click here for more', popup=self.city['city'],
                      icon=folium.Icon(color='purple')).add_to(self.m)

        line = folium.PolyLine(locations=[self.pointA, pointB], weight=5, color='blue')
        CalculateView.m.add_child(line)
        instance.location = self.location
        instance.distance = distance
        instance.save()
        return redirect(instance)


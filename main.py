import streamlit as st
from backend import get_data
import plotly.express as px

st.title("Weather Forecast")
place = st.text_input("Enter the city name and country code separated by a comma",
                      placeholder="e.g. Vancouver, CA")
place = place.split(",")
len_place = len(place)
city = place[0].strip().title()

if len_place == 2:
    country_code = place[1].strip().upper()
elif len_place > 2:
    country_code = None
    st.write("Unable to read location")
else:
    country_code = None

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

if city and country_code and option and days:
    st.subheader(f"{option} for the next {days} days in {city}, {country_code}")

try:
    filtered_data = get_data(city, country_code, days)
    if option == "Temperature":
        dates = [datum["dt_txt"] for datum in filtered_data]
        temperatures = [datum["main"]["temp"] for datum in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Dates",
                                                          "y": "Temperatures"})
        st.plotly_chart(figure)
    elif option == "Sky":
        images = {"Clear": "images/clear.png",
                  "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        sky_conditions = [datum["weather"][0]["main"] for datum in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=100)

except KeyError:
    st.write("Location not found")

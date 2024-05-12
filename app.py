import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def load_model():
    return joblib.load('Dtree.pkl')


def main():
    model = load_model()    

    st.title("Silica Concentration Prediction")
    st.write('Enter the input features to predict silica concentrate:')

    # Input features

    iron_feed = st.number_input('Iron Feed', min_value=0.0, max_value=100.0, value=0.0)
    silica_feed = st.number_input('% Silica Feed', min_value=0.0, max_value=100.0, value=0.0)
    starch_flow = st.number_input('Starch Flow', value=0.0)
    amina_flow = st.number_input('Amina Flow', value=0.0)
    ore_pulp_flow = st.number_input('Ore Pulp Flow', value=0.0)
    ore_pulp_ph = st.number_input('Ore Pulp pH', value=0.0)
    ore_pulp_density = st.number_input('Ore Pulp Density', value=0.0)
    flotation_column_01_air_flow = st.number_input('Flotation Column 01 Air Flow', value=0.0)
    flotation_column_02_air_flow = st.number_input('Flotation Column 02 Air Flow', value=0.0)
    flotation_column_03_air_flow = st.number_input('Flotation Column 03 Air Flow', value=0.0)
    flotation_column_04_air_flow = st.number_input('Flotation Column 04 Air Flow', value=0.0)
    flotation_column_05_air_flow = st.number_input('Flotation Column 05 Air Flow', value=0.0)
    flotation_column_06_air_flow = st.number_input('Flotation Column 06 Air Flow', value=0.0)
    flotation_column_07_air_flow = st.number_input('Flotation Column 07 Air Flow', value=0.0)
    flotation_column_01_level = st.number_input('Flotation Column 01 Level', value=0.0)
    flotation_column_02_level = st.number_input('Flotation Column 02 Level', value=0.0)
    flotation_column_03_level = st.number_input('Flotation Column 03 Level', value=0.0)
    flotation_column_04_level = st.number_input('Flotation Column 04 Level', value=0.0)
    flotation_column_05_level = st.number_input('Flotation Column 05 Level', value=0.0)
    flotation_column_06_level = st.number_input('Flotation Column 06 Level', value=0.0)
    flotation_column_07_level = st.number_input('Flotation Column 07 Level', value=0.0)
    iron_percentage = st.number_input('Iron Percentage', min_value=0.0, max_value=100.0, value=0.0)



    # Prediction

    if st.button('Predict'):
        features = np.array([iron_feed, silica_feed, starch_flow, amina_flow, ore_pulp_flow,
                             ore_pulp_ph, ore_pulp_density, flotation_column_01_air_flow,
                             flotation_column_02_air_flow, flotation_column_03_air_flow,
                             flotation_column_04_air_flow, flotation_column_05_air_flow,
                             flotation_column_06_air_flow, flotation_column_07_air_flow,
                             flotation_column_01_level, flotation_column_02_level,
                             flotation_column_03_level, flotation_column_04_level,
                             flotation_column_05_level, flotation_column_06_level,
                             flotation_column_07_level,iron_percentage]).reshape(1, -1)
        
        pred = model.predict(features)
        st.write('The predicted silica concentrate is:', pred[0])


if __name__ == "__main__":
    main()

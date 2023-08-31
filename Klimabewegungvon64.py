import streamlit as st
import pandas as pd
import altair as alt

st.header("Die Klimabewegung beeinflusst das Leben junger Menschen")
st.subheader("Hat das Engagement junger Menschen für den Klimaschutz Einfluss auf Dein eigenes Leben? - Von den Anteil Ja und ich weiß nicht (64%)")

source = pd.DataFrame({
        'Anteil(%)': [40, 37, 34, 28],
        'Meinung': ['Denken darüber nach, wie sie sich klimafreundlicher verhalten können', 'sorgen sich mehr um die Zukunft', 'versuchen, Freunde & Familie zu klimafreundlicherem Handeln zu bewegen', 'Wollen sich zukünftig noch mehr für den Umwelt und Klimaschutz engagieren']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Meinung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 1010 Befragte; (14 bis 22 Jahre) in Deutschland; 2021
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Umweltbundesamt")
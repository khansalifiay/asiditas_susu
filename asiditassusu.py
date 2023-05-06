import streamlit as st

st.subheader('Hi! :wave:')
st.title('KALKULATOR PENENTUAN ASIDITAS SUSU DENGAN TITRASI ALKALI :glass_of_milk:')
st.markdown('Aplikasi yang bertujuan untuk memudahkan dalam menghitung kadar asam laktat dalam susu.')

st.write('-----')

st.markdown('Penentuan asiditas susu dengan titrasi alkali didasarkan pada reaksi penetralan antara asam dan basa. Terdapat komponen-komponen dalam susu yang bersifat asam dapat bereaksi dengan alkali, misalnya fosfat, protein, dan sebagainya.')

st.write('-----')

st.write('Kelompok 7 :')
col1, col2=st.columns(2)
with col1:
   st.write(''' 
\n :boy: Angga Putra Haryanto (2220445)
\n :boy: Yoga Danuarta (2220499)
\n :boy: Uristyo Utomo (2119005)''')
with col2:
    st.write(''' 
\n :girl: Khansa Alifia Yasmin (2220463)
\n :girl: Maria Asumta P.D.A (2220465)
\n :girl: Nita Agustin Sapitri (2220478)''')

st.write('-----')

st.write('''Rumus penentuan asiditas susu dengan titrasi alkali:
\n%Asam Laktat = ((mL NaOH x N NaOH x 90)/(gram sampel x 1000)) x 100
''')

st.write('-----')

st.write('silahkan masukkan angka')
mLNaOH=st.number_input('volume NaOH')
NNaOH=st.number_input('normalitas NaOH')
gramcontoh=st.number_input('bobot sampel')

if st.button('hitung'):
    persen_asam_laktat=((mLNaOH*NNaOH*90)/(gramcontoh*1000))*100
    st.write(f'kadar asam laktat dalam susu adalah {persen_asam_laktat}%')
else:
    st.write('silahkan tekan tombol hitung')
    
st.write('-----')

st.markdown('Terimakasih sudah menggunakan aplikasi ini, semoga bermanfaat!')
import streamlit as st
import sys
from streamlit import cli as stcli
import pickle

def predict(fname, x_test):
  with open(fname, 'rb') as file:
    clf = pickle.load(file)
  return clf.predict([x_test])

def main():
    st.title('Прогнозирование размеров сварного шва')
    st.write('при электронно-лучевой сварке тонкостенных конструкций аэрокосмического назначения')
    x_test = [None] * 4
    x_test[0] = st.number_input('Величина сварочного тока (IW)')
    x_test[1] = st.number_input('Ток фокусировки электронного пучка (IF)')
    x_test[2] = st.number_input('Скорость сварки (VW)')
    x_test[3] = st.number_input('Расстояние от поверхности образцов до электронно-оптической системы (FP)')
    operation = st.selectbox('Выберите целевую переменную', ['Глубина шва', 'Ширина шва'])
    result = st.button('Предсказать')
    if result:
      if operation == 'Глубина шва':
        pred = predict('mlp1.pkl', x_test)
        st.write(pred)
      elif operation == 'Ширина шва':
        pred = predict('mlp2.pkl', x_test)
        st.write(pred)

if __name__ == '__main__':
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())

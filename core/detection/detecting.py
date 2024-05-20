import subprocess
import os
import sys

sys.path.append(r"C:\Users\ASUS\anaconda3\Lib\site-packages")


class Detecting:
    def __init__(self, predict_path=None):
        self.py_path = r"E:\School\Python_Programme\defect_detection\train.py"
        if not predict_path:
            self.predict_path = r"E:\School\Python_Programme\django_detection/core/media/image/005.png"
        else:
            self.predict_path = predict_path
        self.output_path = r"E:\School\Python_Programme\django_detection\core\media\image"
        self.act_script = r'C:\Users\ASUS\anaconda3\envs\web\ect\conda\activate.d\activate_python.bat'

    def run(self):
        cmd = fr'python "{self.py_path}" --predict_path="{self.predict_path}" --output_path="{self.output_path}" '
        ret = subprocess.run(cmd, cwd=os.getcwd(), shell=True)
        print(ret)

# cmd = r'C:\Users\ASUS\anaconda3\condabin\conda.bat run -n detection python --version'
# cmd = fr'conda run -n detection python "{py_path}" --predict_path="{predict_path}" --output_path="{output_path}" '
# cmd = ['conda.bat', 'activate', 'detection', '&&', 'python', r'E:\School\Python_Programme\defect_detection\print2.py']
# cmd = ['conda.bat', 'activate', 'detection', '&&', 'conda', 'env', 'list']


detect = Detecting()
detect.run()
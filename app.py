from flask import Flask, render_template
import os

app = Flask(__name__)
#我们为Flask这个类设置了实例对象，后面的__name__变量是让Flask知道这个文件、整个模块的名称。
@app.route('/index')
#定义路由，@app.route()装饰器告诉Flask哪个URL应该触发我们的函数，即/是网站的根目录，当访问该根目录时发生以下事件
def index():#定义一个函数，当访问根目录时会执行：
    # 获取所有作品图片（排除封面）
    image_folder = os.path.join('static', 'images')
    #os.path.join()函数用于将多个路径组合成一个路径，'static'和'images'是两个目录名
    #os.listdir()函数返回指定目录下的所有文件和目录名列表
    #这里我们假设所有的图片都存放在static/images目录下
    #如果没有这个目录，Flask会自动创建一个
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    all_images = os.listdir(image_folder)
    profile= 'profile.jpg'
    cover = 'cover.jpg'
    works = [img for img in all_images if img != cover and img != profile]
    #works=img, if img is not=cover, for all img
    return render_template('index.html', cover=cover, works=works)

@app.route('/')
def self():
    return render_template('self.html')

if __name__ == '__main__':
    app.run(debug=True, port=5004) # 使用5004口运行
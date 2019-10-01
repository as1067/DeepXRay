import keras
from keras.layers import Input
from keras.models import Sequential
from prepare_data import PrepareData
import keras_resnet.models

prep = PrepareData()
x,y = prep.prepare()

shape, classes = (448,448,1),15

inp = Input(shape)
model = keras_resnet.models.ResNet50(inp,classes=classes)
model.compile("adam","categorical_crossentropy",["accuracy"])
model.fit(x,y,epochs=100,batch_size=8,validation_split=.2,shuffle=True)





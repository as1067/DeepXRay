import keras
from keras.layers import Input
from keras.optimizers import Adam
from prepare_data import PrepareData
import keras_resnet.models

prep = PrepareData()
x,y = prep.prepare()

shape, classes = (448,448,1),15

inp = Input(shape)
model = keras_resnet.models.ResNet50(inp,classes=classes)
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
model.fit(x,y,epochs=100,batch_size=8,validation_split=.2,shuffle=True)





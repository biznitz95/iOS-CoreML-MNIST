import coremltools

output_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
scale = 1/255.
coreml_model = coremltools.converters.keras.convert('./conv_mnist.h5',
                                                   input_names='image',
                                                   image_input_names='image',
                                                   output_names='output',
                                                   class_labels=output_labels,
                                                   image_scale=scale)

coreml_model.author = 'Shuveb Hussain'
coreml_model.license = 'BSD'
coreml_model.short_description = 'Model to predict handwritten digits'

coreml_model.input_description['image'] = '28x28 grayscale image of digit to predict'
coreml_model.output_description['output'] = 'Digit ASCII value (prediction)'

coreml_model.save('conv_mnist.mlmodel')

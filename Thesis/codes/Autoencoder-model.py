def create_ae_model(input_dim, enc_dim, latent_dim):

    input_layer = Input(shape=(input_dim, ))
    encoder = Dense(enc_dim, activation="tanh", 
                    activity_regularizer=regularizers.l1(10e-5))(input_layer)
    encoder = Dense(latent_dim, activation="relu")(encoder)
    decoder = Dense(enc_dim, activation='relu')(encoder)
    decoder = Dense(input_dim, activation='tanh')(decoder)

    return Model(inputs=input_layer, outputs=decoder)
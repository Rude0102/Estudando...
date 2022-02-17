esta_chovendo= True
hj_chove=False
print("hoje estou com as roupas "+('secas.','molhadas.')[esta_chovendo])
print("Hoje estou com as roupas "+('molhadas'if hj_chove else 'secas'))
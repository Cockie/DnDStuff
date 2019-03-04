# private static EtsNumberField ViaToolReduceLimitNumberField = null;

keys = []
values = []
with open("input.txt") as f:
    for line in f:
        thing = line.split(",")
        keys.append(thing[0])
        values.append(thing[1])

for i in range(0, len(keys)):
    # print("private static EtsNumberField "+keys[i]+"NumberField = null;")
    
    '''print("  /*--------------------------------------------------------------*/")
    print("  private static EtsNumberField get" + keys[i] + "NumberField() {")
    print("    if (" + keys[i] + "NumberField == null) {")
    print("      " + keys[i] + "NumberField = new EtsNumberField(\"hakuto_output." + keys[
        i] + "NumberField\", Uiobj.uiProperties, 15);")
    print("      Parameter par = parameters.get(\"" + keys[i] + "\");")
    print("      if (par.iPrecision == 0) {")
    print("        " + keys[i] + "NumberField.setType(EtsNumberField.TYPE_INTEGER);")
    print("      }")
    print("      else {")
    print("        " + keys[i] + "NumberField.setType(EtsNumberField.TYPE_DOUBLE);")
    print("      }")
    print("      " + keys[i] + "NumberField.setMaxValue(par.dMax);")
    print("      " + keys[i] + "NumberField.setMinValue(par.dMin);")
    print("      " + keys[i] + "NumberField.setvalue(par.dDefault);")
    print("    }")
    print("    return " + keys[i] + "NumberField;")
    print("  }")
    print("")'''
    
    '''print("      innervaluesPanel.add(new EtsLabel(\"hakuto_output." + keys[i] + "\", Uiobj.uiProperties), new GridBagConstraints(0, "+str(i+1)+", 1, 1, 1.0, 0.0, GridBagConstraints.NORTHWEST, GridBagConstraints.HORIZONTAL, new Insets(5, 5, 0, 0), 0, 0));")
    print("      innervaluesPanel.add(get" + keys[i] + "NumberField(), new GridBagConstraints(1, "+str(i+1)+", 1, 1, 1.0, 0.0, GridBagConstraints.NORTHWEST, GridBagConstraints.HORIZONTAL, new Insets(5, 5, 0, 0), 0, 0));")'''
    
    print("    pars = pars + \"" + keys[i] + "=\" + Double.toString(get" + keys[i] + "NumberField().getValue()) + \";\";")

from django.shortcuts import render

from length.forms import LengthConverterForm

convert_to_meter = {
    "centimeter": 0.01,
    "meter": 1.0,
    "mile": 1609.64
}

convert_from_meter = {
    "centimeter": 100,
    "meter": 1.0,
    "mile": 0.000621371
}

def convert(request):
    form = LengthConverterForm()
    if request.GET:
        input_unit = request.GET['input_unit']
        input_value = request.GET['input_value']
        output_unit = request.GET['output_unit']

        meter = convert_to_meter[input_unit] * float(input_value)
        output_value = meter * convert_from_meter[output_unit]

        data = {
            "input_unit":input_unit,
            "input_value":input_value,
            "output_unit":output_unit,
            "output_value": round(output_value, 3)
        }

        form = LengthConverterForm(initial=data)

        return render(request, "length.html", context={"form":form})
    return render(request, "length.html", context={"form":form})

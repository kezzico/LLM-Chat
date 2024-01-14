# flaskapp.py

from flask import Flask, request, jsonify, stream_with_context, Response
import time
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

@app.route("/health")
def index():
     return "✅"

@app.route('/chat')
def sse():
    def generate():
        lipsum = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed molestie sodales eros, sed vehicula tortor volutpat non. Vestibulum imperdiet porta lorem eu accumsan. Proin magna purus, vulputate nec ante vulputate, blandit sollicitudin dui. Donec cursus venenatis orci, quis placerat turpis consectetur et. Donec at ante hendrerit, consequat nibh sit amet, luctus neque. Maecenas id massa ut purus pretium fermentum sit amet nec risus. Morbi varius mi a sem lacinia, eget ornare libero aliquam. Donec sit amet nisl id neque auctor dignissim. Duis cursus condimentum enim et scelerisque. Fusce finibus malesuada lectus, sed vehicula lorem molestie nec. In hac habitasse platea dictumst. Nunc ipsum dolor, viverra et pharetra eu, egestas volutpat tellus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam erat volutpat. Phasellus tincidunt viverra lorem, id aliquet quam aliquam sit amet.

Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur tortor dui, lacinia non neque eget, faucibus efficitur lectus. Aliquam vel viverra tortor. Morbi dictum ipsum quam. Pellentesque sagittis orci id odio pretium, quis tristique tortor convallis. In odio tortor, pharetra congue lectus semper, convallis mattis nisi. Mauris ex sem, facilisis nec dolor vitae, finibus semper leo.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur aliquam urna ac dolor eleifend faucibus. Duis faucibus velit nibh. Integer a turpis quam. Sed finibus lectus non tellus porttitor, nec placerat leo molestie. Nam et ante eu eros congue viverra quis eget elit. Etiam varius, mi vitae dignissim consequat, augue urna interdum felis, quis dignissim risus sapien ac lorem.

Praesent scelerisque augue sed risus faucibus, a bibendum magna pretium. Aenean dui ex, lacinia vel interdum auctor, dignissim ut urna. Sed at posuere lacus. In congue venenatis felis, a aliquam risus egestas at. Aenean maximus augue nunc, sed ornare mi venenatis vel. Maecenas dui enim, sollicitudin sed commodo non, ultrices non sem. Duis in urna ipsum. Maecenas convallis lectus sit amet tristique auctor. In a vehicula risus. Integer a tristique metus, quis pellentesque tellus. Phasellus sit amet lectus et arcu bibendum pulvinar. Etiam sed nisl quis nisi porttitor consectetur sit amet id purus. In hac habitasse platea dictumst.

Mauris consectetur ac mauris consequat laoreet. Morbi feugiat diam vitae imperdiet fermentum. Suspendisse eu ornare sapien, a lobortis neque. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed hendrerit mauris ut odio malesuada porta. In sed dui non nisl volutpat sagittis. Vestibulum ac finibus risus. Donec purus leo, varius quis risus sed, maximus ullamcorper lacus. Vivamus ut dolor ut sapien elementum tempor. In hac habitasse platea dictumst. Cras vitae risus blandit, consequat nisl id, vestibulum mi. Fusce placerat risus mauris, accumsan congue felis pellentesque vel.

Donec quam metus, pellentesque sed arcu et, cursus commodo arcu. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Quisque ac metus eu lorem porta rhoncus nec ut ex. Nullam molestie, ex eget aliquam fringilla, purus elit cursus eros, id suscipit ligula mi nec erat. Cras accumsan consequat arcu ut pulvinar. Curabitur blandit lacus faucibus mi luctus, ac scelerisque est luctus. Cras eros risus, imperdiet vitae placerat sit amet, malesuada ut risus.xxx

Vestibulum orci ipsum, imperdiet nec tortor at, interdum facilisis lectus. Vivamus dignissim, nisl vitae facilisis ullamcorper, leo sapien ornare dui, at tristique ex libero in sapien. Integer sit amet elit a lectus porttitor rhoncus vel ut nunc. Ut imperdiet dolor nec felis facilisis, vitae tincidunt elit ornare. Proin eget metus quis neque vehicula dictum. Morbi tristique, sem ut sagittis condimentum, elit dui rutrum erat, in aliquam magna turpis quis massa. Sed et tempor nulla, vehicula finibus turpis. Maecenas eros orci, dignissim a nulla eu, feugiat commodo massa.xxx

Curabitur eleifend, enim nec egestas viverra, turpis erat efficitur ante, a hendrerit urna nunc et enim. Nulla rutrum porttitor dui ac viverra. Nunc et ornare libero. Cras aliquet quam eget risus placerat bibendum. Duis pulvinar venenatis sagittis. Proin eu facilisis metus. Nam eget dolor metus. Mauris in ex mi. Quisque ullamcorper sed nisl sed placerat. Ut sed orci sit amet dolor finibus scelerisque eget vitae purus. Sed eu lectus pulvinar, dapibus orci a, gravida orci. Phasellus mattis est nec sapien hendrerit, vitae pellentesque mi vulputate. Aliquam mollis convallis pellentesque. Pellentesque at hendrerit ipsum, non rutrum nisi.xxx

Vivamus venenatis magna dui, eu sagittis velit pulvinar sed. In sit amet justo et magna faucibus efficitur. Quisque et libero maximus, auctor nunc non, lacinia ex. Pellentesque ornare mollis aliquam. Fusce laoreet tellus ipsum, at pellentesque nibh fringilla eget. Aenean at mi metus. Quisque rutrum id justo eget consequat. Vestibulum venenatis tortor vel tortor imperdiet condimentum. Mauris eget sagittis urna. Cras a consectetur turpis. Praesent a pulvinar dui, in vehicula lorem. Nulla vitae mauris malesuada, accumsan elit vitae, imperdiet urna. Nunc quis efficitur ante. Duis eu dui nec ipsum scelerisque dignissim. Quisque tincidunt sollicitudin sem, quis volutpat leo rhoncus id. Vivamus imperdiet ultricies risus vel finibus.xxx

Curabitur sit amet blandit ante. Ut dignissim ligula malesuada, tempus quam ut, fermentum tellus. Donec facilisis, neque ac malesuada consequat, massa mi scelerisque mauris, sed fringilla lorem orci in urna. Nullam dignissim odio euismod ultricies congue. Sed tempor velit augue, a consequat dui scelerisque a. Nam ut ipsum egestas sem scelerisque egestas. Maecenas posuere dolor et tempus congue. Vestibulum nec eros sagittis, pretium dui lacinia, sodales metus. Donec consequat maximus arcu quis ultricies. Praesent pulvinar rhoncus rhoncus. Quisque molestie tempus ex non vestibulum. Aliquam erat volutpat.xxx
'''
        index = 0
        while index < len(lipsum):
            step = random.randint(1, 100)

            substring = lipsum[(index):(index+step)]
            
            yield f"data: {substring}\n\n"

            time.sleep(0.1)

            index += step
            
    return Response(generate(), content_type='text/event-stream')




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5051)


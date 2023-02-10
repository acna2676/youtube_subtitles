from youtube_transcript_api import YouTubeTranscriptApi

transcript_list = YouTubeTranscriptApi.list_transcripts("u21W_tfPVrY")

text_combined = ''
for transcript in transcript_list:
    for tr in transcript.fetch():
        # print(tr) # {'text': '字幕のテキスト情報', 'start': 字幕の開始時間, 'duration': 字幕が表示されている時間}
        text_combined += tr['text'] + ' '

# 結合したテキストファイルを生成
with open('result.txt', 'w') as f:
    f.write(text_combined)

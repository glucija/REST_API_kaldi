## REST API KALDI

First build Docker image:

``` docker build -t kaldi-asr .```

Run Docker container:

``` docker run -d --name kaldi-asr-server -'your_path/asr:/asr -p 5000:5000 kaldi-asr ```

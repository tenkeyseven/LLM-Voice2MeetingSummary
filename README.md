# LLM-Voice2MeetingSummary

LLM-Voice2MeetingSummary is a project that aims to automate the process of generating meeting summaries from voice recordings using OpenAI's GPT model, LLM. This project is inspired by the article [here](https://mp.weixin.qq.com/s/EIJqlbNcOWBVNfi4QVaVBQ) and the OpenAI tutorial on meeting minutes [here](https://platform.openai.com/docs/tutorials/meeting-minutes).

## Overview

This repository consists of two main parts:

1. Voice Segmentation: In this step, the original .wav voice file is processed to identify and separate the conversations between speakers. This process requires human intervention to set time spots where the conversations switch between the two parties.

2. Summary Generation: Once the voice recordings have been segmented, OpenAI's GPT model, LLM, is utilized to generate concise meeting summaries. The model analyzes the transcribed conversations and extracts key discussions and outcomes, providing participants with an easily accessible summary of the meeting.

## Installation

To use this project, please follow these steps:

1. Clone the repository: `git clone https://github.com/tenkeyseven/LLM-Voice2MeetingSummary.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the necessary environment variables for the OpenAI API access.

## Usage

1. Prepare the voice recording in .wav format.
2. Run the voice segmentation script and follow the instructions to set time spots for switching between colleagues and leaders.
3. Once the segmentation is complete, run the summary generation script using LLM to obtain the meeting summary.

Please note that the OpenAI API access is required for the LLM model. Ensure that you have the necessary credentials and permissions.

## Contributing

Welcome discussing! seeking for ideas, bug reports, or enhancements, please open an issue or submit a pull request.


## README.CN

LLM-Voice2MeetingSummary 是一个项目，旨在利用 OpenAI 的 GPT 模型 LLM，从语音录音中自动生成会议摘要。该项目受到了[机器之心](https://mp.weixin.qq.com/s/EIJqlbNcOWBVNfi4QVaVBQ)和 OpenAI 的会议纪要教程的启发，教程链接[在此](https://platform.openai.com/docs/tutorials/meeting-minutes)。

## 概述

该存储库包含两个主要部分：

1. 语音分割：在此步骤中，原始的 .wav 语音文件将被处理，以识别并分离对话者之间的对话。这一过程需要人工标记时间，在对话切换时设置时间点。

2. 摘要生成：一旦语音录音被分割，利用 OpenAI 的 GPT 模型 LLM 来生成简洁的会议摘要。模型分析转录的对话，并提取关键讨论和结果，为参与者提供易于访问的会议摘要。

## 安装

要使用该项目，请按照以下步骤进行：

1. 克隆存储库：`git clone https://github.com/tenkeyseven/LLM-Voice2MeetingSummary.git`
2. 安装所需的依赖项：`pip install -r requirements.txt`
3. 设置必要的环境变量以访问 OpenAI API。

## 使用方法

1. 准备 .wav 格式的语音录音。
2. 运行语音分割脚本，并按照说明设置同事和领导之间的切换时间点。
3. 完成分割后，使用 LLM 运行摘要生成脚本，获取会议摘要。

LLM 模型需要访问 OpenAI API。请确保具备必要的凭据和权限。


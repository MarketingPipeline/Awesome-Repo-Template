# Awesome-Repo-Template [![Awesome](https://awesome.re/badge.svg)](https://github.com/MarketingPipeline/Awesome-Repo-Template/)

<a href="https://github.com/MarketingPipeline/Awesome-Repo-Template/">
<img height=350 alt="Repo Banner - Awesome Repo Template" src="https://capsule-render.vercel.app/api?type=waving&color=c4a2bd&height=300&section=header&text=Awesome Repo Template&fontSize=70&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Easily setup your next repo!&descAlignY=60&descAlign=50"></img></a>

<p align="center">
  <b>A awesome repo template to kick-start your next project</b>

  <br>
  <small> <b><i>Show your support!</i> </b></small>
  <br>
   <a href="https://github.com/MarketingPipeline/Awesome-Repo-Template">
    <img title="Star on GitHub" src="https://img.shields.io/github/stars/MarketingPipeline/Awesome-Repo-Template.svg?style=social&label=Star">
  </a>
  <a href="https://github.com/MarketingPipeline/Awesome-Repo-Template/fork">
    <img title="Fork on GitHub" src="https://img.shields.io/github/forks/MarketingPipeline/Awesome-Repo-Template.svg?style=social&label=Fork">
  </a>
   </p>  


## Features:

- A configurable workflow action to:  
  - update all links with your own with EASE!
  - update Code Of Conduct E-mail with your own!
  - generate a table of contents in your README
  - generate a star-gazer metrics image
- Time Saving Files:
  - [Pull request template](.github/pull_request_template.md)
  - Issue templates for [bug reports](.github/ISSUE_TEMPLATE/bug_report.yaml) and
    [feature requests](.github/ISSUE_TEMPLATE/feature_request.yaml)
  - [Contributor guidelines](CONTRIBUTING.md)
  - [Code of Conduct](CODE_OF_CONDUCT.md)
  - [To-Do List](.github/TO_DO.md)
  - [README](README.md)
  - [License file](LICENSE) 




## Example and Usage




	
 <br>
<details><summary>How to use this <b>template</b>:</summary>
 <br>		
 
 To run any of these tasks you MUST be in the <b>Actions section</b>
 
 <details><summary>How to find the <a href="https://github.com/MarketingPipeline/Awesome-Repo-Template/actions"><b>Action</b></a></summary>
 
<a href="https://github.com/MarketingPipeline/Awesome-Repo-Template/actions"> ![image](https://user-images.githubusercontent.com/86180097/177446180-b71e50d1-df9d-4ef8-8d78-91184702cff0.png) </a>

</details>	

<br>	 
<br>	 
	
<details><summary>How to replace all <b>links</b> with your own:</summary>
<br>	
	
Edit the [repo_config.json](.github/py_repo_tools/repo_config.json) file & set the value for "REPLACE_TEXT_WITH" - to your username & repo name like the following example 

       MyUserName/My-Repo-Name

And run the Repo Generator in Actions - set "Update all links" to <code>checked</code>
 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	
</details>

<br>	 
<br>	 
	
<details><summary>How to replace <b>e-mail</b> in <a href="CODE_OF_CONDUCT.md">Code of Conduct</a> with your own:</summary>
<br>	
	
Edit the [repo_config.json](.github/py_repo_tools/repo_config.json) file & set the value for "CODE_OF_CONDUCT_EMAIL" - to your e-mail address like the following example. 

       hello_world@github.com

And run the Repo Generator in Actions- set "Update Code Of Conduct Info" to <code>checked</code>
 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	
</details>
 <br>		
 
	
<br>	 
<br>	 
	
<details><summary>How to generate <b>Table Of Contents</b>:</summary>
<br>	
To generate tables of contents automatically use anywhere in your README.md file a comment like so

   
&lt;!-- toc -->

&lt;!-- tocstop -->


And when running the Repo Generator in Actions - set "Generate Table Of Contents" to <code>checked</code>


<b><i>WARNING:</i></b> Only 1 table of contents can be generated in a README - if you use more than one you WILL face problems. 
 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	
</details>


 <br>		
 
	
<br>	 
<br>	 
	
<details><summary>How to Generate a <b>Metrics Image</b>:</summary>
<br>	
 
Create a Personal Access Token & create a repo secret called "METRICS_TOKEN" & when running the Repo Generator - set "Generate Metrics Image File" to <code>checked</code> 

You will have an image generated that looks like this!

<img src="stargazers-metrics.svg"></img>

It will be placed in the main repo under the filename <code>stargazers-metrics.svg</code> 

<i>Note:</i> if someone knows how to change this please make a pull request with the image placed to .github folder!


 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	
</details>


<br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>		
</details>
	
<br>	 
	
<details><summary>Shield.io Buttons:</summary>
<br>

<!--Copy & paste whatever buttons you need!-->

_Repo metadata_

	
[![Github license](https://img.shields.io/github/license/MarketingPipeline/Awesome-Repo-Template.svg "Github license")](https://github.com/MarketingPipeline/Awesome-Repo-Template/blob/master/LICENSE)
[![Open issues](https://img.shields.io/github/issues/MarketingPipeline/Awesome-Repo-Template.svg "Open issues")](https://github.com/MarketingPipeline/Awesome-Repo-Template/issues)
[![Closed issues](https://img.shields.io/github/issues-closed/MarketingPipeline/Awesome-Repo-Template.svg "Closed issues")](https://github.com/MarketingPipeline/Awesome-Repo-Template/issues?utf8=✓&q=is%3Aissue+is%3Aclosed)
[![Open Pull Requests](https://img.shields.io/github/issues-pr/MarketingPipeline/Awesome-Repo-Template.svg "Open Pull Requests")](https://github.com/MarketingPipeline/Awesome-Repo-Template/pulls)
[![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed/MarketingPipeline/Awesome-Repo-Template.svg "Closed Pull Requests")](https://github.com/MarketingPipeline/Awesome-Repo-Template/pulls?utf8=✓&q=is%3Apr+is%3Aclosed)
[![Commit activity](https://img.shields.io/github/commit-activity/m/MarketingPipeline/Awesome-Repo-Template.svg "Commit activity")](https://github.com/MarketingPipeline/Awesome-Repo-Template/graphs/commit-activity)
[![GitHub contributors](https://img.shields.io/github/contributors/MarketingPipeline/Awesome-Repo-Template.svg "Github contributors")](https://github.com/MarketingPipeline/Awesome-Repo-Template/graphs/contributors)
[![Last commit](https://img.shields.io/github/last-commit/MarketingPipeline/Awesome-Repo-Template.svg "Last commit")](https://github.com/MarketingPipeline/Awesome-Repo-Template/commits/master)
[![GitHub tag](https://img.shields.io/github/tag/MarketingPipeline/Awesome-Repo-Template?include_prereleases=&sort=semver&color=blue)](https://github.com/MarketingPipeline/Awesome-Repo-Template/releases/)



_Social buttons_

[![MarketingPipeline - Awesome-Repo-Template](https://img.shields.io/static/v1?label=MarketingPipeline&message=Awesome-Repo-Template&color=blue&logo=github)](https://github.com/MarketingPipeline/Awesome-Repo-Template "Go to GitHub repo")
[![stars - Awesome-Repo-Template](https://img.shields.io/github/stars/MarketingPipeline/Awesome-Repo-Template?style=social)](https://github.com/MarketingPipeline/Awesome-Repo-Template)
[![forks - Awesome-Repo-Template](https://img.shields.io/github/forks/MarketingPipeline/Awesome-Repo-Template?style=social)](https://github.com/MarketingPipeline/Awesome-Repo-Template)



_Call-to-Action buttons_



[![Use this template](https://img.shields.io/badge/Generate-Use_this_template-2ea44f?style=for-the-badge)](https://github.com/MarketingPipeline/Awesome-Repo-Template/generate)

[![View site - GH Pages](https://img.shields.io/badge/View_site-GH_Pages-2ea44f?style=for-the-badge)](https://marketingpip.github.io/Awesome-Repo-Template/)


_Documentation button_


[![view - Documentation](https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge)](/README.MD "Go to project documentation")


_Custom button_

<img alt="Custom Shield.io Button" src="https://img.shields.io/badge/Custom-Button-blue.svg?style=flat-square"></img>	


<br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	 <br>	
</details>
	
<br>	 
	 

<details><summary>Auto Generated Table Of Contents <b> Demo</b>:</summary>
<br>
<!------- Table Of Contents Will Auto Generate In Side Of Here ---- >

<!-- toc -->

- [Features:](#features)
- [Example and Usage](#example-and-usage)
- [Contributing ![GitHub](https://img.shields.io/github/contributors/MarketingPipeline/Awesome-Repo-Template)](#contributing-githubhttpsimgshieldsiogithubcontributorsmarketingpipelineawesome-repo-template)
- [License ![GitHub](https://img.shields.io/github/license/MarketingPipeline/Awesome-Repo-Template)](#license-githubhttpsimgshieldsiogithublicensemarketingpipelineawesome-repo-template)

<!-- tocstop -->

</details>









## Contributing <a href="https://github.com/MarketingPipeline/Awesome-Repo-Template/graphs/contributors"> ![GitHub](https://img.shields.io/github/contributors/MarketingPipeline/Awesome-Repo-Template) </a>

Want to improve this template? Create a pull request with detailed changes / improvements! If approved you will be added to the list of contributors of this awesome repo template!

See also the list of
[contributors](https://github.com/MarketingPipeline/Awesome-Repo-Template/graphs/contributors) who
participate in this project.

## License <a href="LICENSE"> ![GitHub](https://img.shields.io/github/license/MarketingPipeline/Awesome-Repo-Template) </a>

This project is licensed under the MIT License - see the
[LICENSE.md](https://github.com/MarketingPipeline/Awesome-Repo-Template/blob/main/LICENSE) file for
details.





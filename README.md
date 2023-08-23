<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">AppleWalletPassCreator</h3>

  <p align="center">
    Apple Wallet Pass creation process python package
    <br />
    <a href="https://github.com/RolandSobczak/ApplePassCreator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/RolandSobczak/ApplePassCreator">View Demo</a>
    ·
    <a href="https://github.com/RolandSobczak/ApplePassCreator/issues">Report Bug</a>
    ·
    <a href="https://github.com/RolandSobczak/ApplePassCreator/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This package provide simple tools for Apple Wallet pass creation.
Only requirement is to install openssl command which is available out of the box on the most of
linux distribution and macOS


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Apple Wallet Cert

To install pass on Apple device You need to generate Apple Wallet cert.
Unfortunately to generate this cert You need to enroll Apple Developer subscription which cost is 99$ per year.
I do not find any way to omit this paywall, even if You just want to play with this technology for testing purposes.

I have created tutorial about all process of cert generation.
Here is the [link](https://github.com/RolandSobczak/AppleWalletPassCreation)


### Prerequisites

This package calls `openssl` command under the hood. Apple Wallet pass creation process need PKCS7 algorithm.
I didn't find any popular package in python, so IMO calling openssl is the most secure way.

**Note that:** PKCS7 not working good in latest openssl command version.
When I was trying to use latest version I was getting errors and empty result file.
I recommend to use this package with **openssl ver 1.1**.

### Installation
```shell
pip install git+https://github.com/RolandSobczak/ApplePassCreator.git
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You can find examples of usage in `examples/` folder.
Remember to read docstrings before run, because You have to meet some requirements to create correct pass.
I recommend to put all Your certs in `examples/certs` to start play with this package in shorter way.
Another step is to download samples. You can download it
[here] ()

<!-- ROADMAP -->
## How it works

Before I created this package I had published simple
[tutorial](https://github.com/RolandSobczak/AppleWalletPassCreation) for creating Apple Wallet Passes.
I recommend to play with it before to get general look on how this process works.
This project just implement all steps from this tutorial in python.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Roland Sobczak - [@linkedin_handle](https://www.linkedin.com/in/roland-sobczak/) - rolandsobczak@icloud.com

Project Link: [https://github.com/RolandSobczak/ApplePassCreator](https://github.com/RolandSobczak/ApplePassCreator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Apple Wallet Passes tutorial](https://github.com/RolandSobczak/AppleWalletPassCreation)
* [OpenSSL docs](https://www.openssl.org/docs/)
* [Apple Wallet Passes docs](https://developer.apple.com/documentation/walletpasses/building_a_pass)
* [Apple Wallet Pass validator](https://pkpassvalidator.azurewebsites.net)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/RolandSobczak/ApplePassCreator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/RolandSobczak/ApplePassCreator/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/RolandSobczak/ApplePassCreator/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/RolandSobczak/ApplePassCreator/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/RolandSobczak/ApplePassCreator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/roland-sobczak/

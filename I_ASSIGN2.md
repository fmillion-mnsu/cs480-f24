# Individual Assignment 2 - S3

In this exercise you will learn about S3 Object Storage.

This assignment does not require you to use a live cloud service. However, it does require that you run the MinIO software locally on your machine. **The easiest and most convenient way to do this is by using Docker.** 

If you can use Docker on your machine, the following Docker command will start up MinIO:

    docker run -p 9000:9000 -p 9001:9001 --name minio -d quay.io/minio/minio server /data --console-address ":9001"

> This configuration will not persist data if you delete the container. If you want your MinIO data to be preserved, even if you delete and recreate the container, use a **volume mount** to connect a local directory to `/data` within the container.

If you are unable to run Docker or don't wish to use it for some reason, you can follow [these instructions](https://min.io/docs/minio/windows/index.html) to install MinIO natively on your platform. Use the tabs to select your platform.

> **The `mc` MinIO Client**
>
> There is also a command line tool that ships with MinIO called `mc`. This tool can be used to interact with MinIO from the command line and is very useful for scripting and automation.
>
> You should not need to use `mc` for this project, but if you want to install it to learn how it works, [here are the instructions](https://min.io/docs/minio/linux/reference/minio-mc.html).

## Assignment Requirements

You will build a simple application **in a language of your choice** that can:

* Upload a file to your S3 server
* Download a file from your S3 server
* List available files on the server

You may use any appropriate language you feel comfortable coding in - Python, Java, C#, NodeJS, etc. are all acceptable.

Since S3 can actually be used to host a website directly, you can upload an HTML file to your S3 server using your tool, or even get creative and auto-generate some HTML before uploading it. You can then view the HTML in a browser by simply pointing your browser at the correct URL within the S3 server!

Your application must contain the following characteristics:

* Allow the user to choose which function to run - upload, download or list. 
  * You can implement this as three separate scripts if you find it easier, or you could implement a GUI-based application in e.g. Windows Forms or TKinter to make it one application
* Provide a mechanism for specifying the four key values needed for an S3 server: the URL, the bucket name, the **access key** (analogous to a username), and the **secret key** (analogous to a password).
  * You could prompt the user for these or you could allow the user to provide them some other way - e.g. environment variables, command line options, a config file, etc.
* Follow basic best coding practices - use appropriate method/function names, use classes where appropriate and so on.

> **Important**: Whether you run MinIO directly or via Docker, you should be able to use `http://localhost:9000/<bucket_name>` as the S3 base URL. The access code and secret key default to `minioadmin` and `minioadmin` for the root user.
>
> You can access the admin console by visiting <http://localhost:9001>.
>
> The MinIO server does not come with any buckets created. **Use the admin console to create a bucket** - you can't upload any files to an S3 server without a bucket!

For whichever language you are using, **investigate available libraries for interacting with S3**. For example, Python has [minio Python library](https://min.io/docs/minio/linux/developers/python/minio-py.html) offering Pythonic access to S3 servers (including, *but not limited to*, MinIO). If your language offers a library or even multiple libraries, use them - don't bother with crafting HTTP requests by hand! (It's tedious, error prone and will make your the project harder to complete!)

## Submission

Zip your code files and submit them to the D2L dropbox.

The due date for this assignment is **Friday, November 22** at **11:59 PM**.

This is an **individual assignment** - everyone must submit their own work. You may help each other but you may not share code with classmates.

# 90-Day Cloud Engineer Roadmap (Reference)

> **Source:** External roadmap provided for comparison  
> **Date Added:** October 5, 2025  
> **Status:** Reference material for enhancement ideas

This is an intensive 90-day plan designed for a motivated CS student to go from a solid foundation to being interview-ready for a junior Cloud/DevOps role.

---

## Prerequisites:
 * Comfortable with the Linux command line (you are, using Arch).
 * Basic understanding of Python syntax (loops, functions, data structures).
 * A GitHub account and basic git knowledge.
 * A willingness to learn and be challenged, dedicating 1-3 hours per day.

**Disclaimer:** This roadmap is aggressive. Don't be discouraged if you need to spend more time on a specific topic. The goal is progress, not perfection. The weeks are guides; the concepts are the requirements.

---

## Month 1: The Bedrock - Fundamentals & Automation (Days 1-30)

**Goal:** Master the tools and concepts before touching the cloud. This month is about becoming a power user of your own system and learning the language of automation.

### Week 1: Advanced Linux & Shell Scripting (Days 1-7)

 * [ ] Deepen Shell Knowledge: Master `grep`, `awk`, `sed`, and `jq` for text processing and data extraction from the command line.
 * [ ] Process Management: Understand `ps aux`, `top`/`htop`, `nice`, `kill`, and signals. Learn about `systemd` to manage services.
 * [ ] Permissions Mastery: Solidify your understanding of `chmod`, `chown`, and file permissions (user, group, other).
 * [ ] **Project:** Write a non-trivial bash script. 
   - **Idea:** A script that backs up a specified directory into a `.tar.gz` archive, names it with the current date (`backup-YYYY-MM-DD.tar.gz`), and stores it in a `backups` folder.

---

### Week 2: Practical Networking Concepts (Days 8-14)

 * [ ] **IP & Subnetting:** Learn CIDR notation. Use an online subnet calculator to understand how to divide networks. This is crucial for the cloud.
 * [ ] **DNS Deep Dive:** What happens when you type `google.com`? Learn the roles of A records, CNAMEs, etc. Use `dig` and `nslookup` extensively.
 * [ ] **HTTP/S & APIs:** Understand the difference between HTTP verbs (GET, POST, PUT, DELETE). Use `curl` to make requests to public APIs from your terminal. Inspect headers.
 * [ ] **Theory:** Whiteboard the concepts of a Load Balancer, a Firewall (Security Group), and a Public vs. Private Subnet.

---

### Week 3: Python for Cloud Automation (Days 15-21)

 * [ ] **Key Libraries:** Focus on libraries used for automation.
   * `requests`: For interacting with APIs.
   * `subprocess` & `os`: For running shell commands and interacting with the OS.
   * `argparse`: For building your own Command-Line Interface (CLI) tools.
   * `boto3`: The AWS SDK for Python. Just install it and look at the documentation for now.
 * [ ] **Virtual Environments:** Never work without them. Master `python -m venv myenv` and `source myenv/bin/activate`. Use a `requirements.txt` file.
 * [ ] **Project:** Convert your "Day 6" or any other Python script into a proper CLI tool using argparse. 
   - **Idea:** A tool that takes a GitHub username as an argument and uses the GitHub API to list that user's public repositories.

---

### Week 4: Mastering Git & GitHub (Days 22-30)

 * [ ] **Branching Strategy:** Learn the "Gitflow" branching model conceptually (feature branches, develop, main).
 * [ ] **Practice Merging:** Create feature branches, make changes, and `git merge` them back. Intentionally create a merge conflict and learn how to resolve it.
 * [ ] **rebase vs merge:** Understand the difference. Use `git rebase -i` to clean up your commit history on a feature branch before merging.
 * [ ] **GitHub Workflow:** Fork a public repository, clone it, make a change, and open a Pull Request (PR). Learn how to review PRs and request changes.

---

## Month 2: The Cloud & Containers (Days 31-60)

**Goal:** Get hands-on with a major cloud provider and master the fundamental unit of modern deployment: the container.

### Week 5: Introduction to AWS (Days 31-37)

 * [ ] **Create Account:** Sign up for the AWS Free Tier.
 * [ ] **Security First:** Immediately set up Multi-Factor Authentication (MFA) on your root account.
 * [ ] **Billing Alerts:** Configure AWS Budgets and billing alerts to avoid surprises.
 * [ ] **IAM Deep Dive:** This is the most critical security service.
   * Create an IAM user for yourself with administrative privileges and stop using the root account.
   * Learn the difference between Users, Groups, Roles, and Policies.

---

### Week 6: Core AWS Services (Days 38-44)

 * [ ] **EC2 (Compute):** Launch your first `t2.micro` Linux EC2 instance. SSH into it from your Arch terminal.
 * [ ] **Security Groups:** Configure the instance's Security Group (firewall) to only allow SSH (port 22) and HTTP (port 80) from your IP address.
 * [ ] **S3 (Storage):** Create an S3 bucket. Learn to upload, download, and delete files using both the web console and the `aws-cli`.
 * [ ] **EBS (Volumes):** Understand that EC2 instances use EBS volumes for their root disk. Learn how to create and attach an additional EBS volume to your instance.

---

### Week 7: Containerization with Docker (Days 45-51)

 * [ ] **Docker Fundamentals:** Install Docker on your Arch machine. Understand the difference between an Image and a Container.
 * [ ] **Dockerfile:** Take your Python CLI tool from Week 3 and write a Dockerfile for it.
 * [ ] **Build & Run:** Use `docker build` to create an image. Use `docker run` to run it as a container. Master `docker ps`, `docker logs`, `docker exec`.
 * [ ] **Project:** Use `docker-compose` to define and run a two-container application: your Python app and a `redis` container. Have the Python app connect to Redis.

---

### Week 8: Integrating Docker & AWS (Days 52-60)

 * [ ] **Install AWS CLI:** Install and configure the `aws-cli` on your local machine with the IAM user credentials you created.
 * [ ] **ECR (Elastic Container Registry):** Create a private ECR repository in AWS.
 * [ ] **Login & Push:** Learn how to authenticate your Docker client to ECR.
 * [ ] **Push your Image:** Tag your Python application's Docker image from Week 7 with the ECR repository URI and `docker push` it to AWS. **This is a major milestone.**

---

## Month 3: Automation & Infrastructure at Scale (Days 61-90)

**Goal:** Stop doing things manually. Define everything as code and build automated pipelines to deploy it.

### Week 9: CI/CD with GitHub Actions (Days 61-67)

 * [ ] **Concepts:** Understand the concepts of Continuous Integration (automating tests) and Continuous Deployment (automating releases).
 * [ ] **Your First Workflow:** Create a `.github/workflows/main.yml` file in your Python project repository.
 * [ ] **Build Pipeline:** Configure the workflow to trigger on a `git push`. It should:
   * Check out your code.
   * Set up Python.
   * (Optional but good practice) Run a linter like `flake8` or tests with `pytest`.
 * [ ] **Project:** Extend your workflow to be a full CI/CD pipeline. Add steps to log in to AWS ECR, build your Docker image, and push it to the ECR repository you created in Week 8. Use GitHub Secrets to store your AWS credentials securely.

---

### Week 10: Infrastructure as Code (IaC) with Terraform (Days 68-74)

 * [ ] **Install Terraform:** Install Terraform on your Arch machine.
 * [ ] **Terraform Basics:** Understand the provider/resource model. Learn the core workflow: `terraform init`, `terraform plan`, `terraform apply`, `terraform destroy`.
 * [ ] **State Management:** Understand what the Terraform state file (`.tfstate`) is and why it's important.
 * [ ] **Project:** Write a Terraform configuration (`.tf` file) that provisions an AWS EC2 instance and a Security Group. Destroy it and bring it back up several times to appreciate the power and consistency of IaC.

---

### Week 11: Introduction to Kubernetes (Days 75-81)

 * [ ] **Concepts:** Kubernetes is complex. Focus on understanding the "why". What problems does it solve over plain Docker?
 * [ ] **Local Cluster:** Install `minikube` or `k3d` and `kubectl` on your machine to run a local Kubernetes cluster.
 * [ ] **Core Objects:** Learn about the most important K8s objects by writing YAML manifests for them:
   * **Pod:** The smallest unit of deployment.
   * **Deployment:** Manages a set of replica Pods.
   * **Service:** Exposes your application as a network service.
 * [ ] **Project:** Deploy your Python application's container (from ECR) onto your local Kubernetes cluster. Access it using the Service you created.

---

### Week 12: Capstone Project & Review (Days 82-90)

 * [ ] **Project Goal:** Build an end-to-end, automated deployment.
   * **Application:** A simple "Hello World" Python web app using Flask or FastAPI.
   * **IaC:** Use Terraform to provision an AWS ECR repository and a single EC2 instance with Docker installed.
   * **CI/CD:** Create a GitHub Actions pipeline that on `git push`:
     * Tests the code.
     * Builds the Docker image.
     * Pushes the image to the ECR repo created by Terraform.
 * [ ] **Manual Deployment (Final Step):** SSH into the EC2 instance created by Terraform, pull your new image from ECR, and run it. Access the web app from your browser. (Automating this last step with Ansible or user-data scripts is the next level).
 * [ ] **Final Days:** Clean up your GitHub repositories. Write excellent `README.md` files for your best projects. Explain what they do, what you learned, and how to run them. **Your GitHub is now your resume.**

---

## Beyond 90 Days

 * **Monitoring:** Learn Prometheus & Grafana.
 * **Managed Kubernetes:** Deploy your app to a managed service like AWS EKS using Terraform.
 * **DevSecOps:** Learn about scanning your Docker images for vulnerabilities and managing secrets.
 * **Advanced Python:** Learn boto3 in depth to write complex automation scripts for AWS.

---

## 📝 Notes

This roadmap serves as reference material. See `NEW_90DAY_ROADMAP_ANALYSIS.md` for detailed comparison with our ULTIMATE_CLOUD_DEVOPS_ROADMAP.md and integration recommendations.

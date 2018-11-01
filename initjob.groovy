import hudson.model.*
def installlist = System.getenv("installlist")

stage('输出安装列表'){
            echo $installlist
        }

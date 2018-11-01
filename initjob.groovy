import hudson.model.*
import hudson.AbortException
import hudson.console.HyperlinkNote
import java.util.concurrent.CancellationException

user = hudson.model.User.get('username')
prop = user.getProperty(jenkins.security.ApiTokenProperty.class)
println(prop.getApiToken())

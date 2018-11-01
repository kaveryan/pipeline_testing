import hudson.model.*
import hudson.AbortException
import hudson.console.HyperlinkNote
import java.util.concurrent.CancellationException

// Retrieve parameters of the current build
def installlist = build.buildVariableResolver.resolve("installlist")
println "installlist=$installlist"

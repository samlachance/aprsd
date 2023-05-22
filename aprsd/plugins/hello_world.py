
from aprsd import plugin
from aprsd.utils import trace


LOG = logging.getLogger("APRSD")


class HelloWorldPlugin(plugin.APRSDRegexCommandPluginBase):
    """Hello World"""

    command_regex = r"^([hw])"
    command_name = "hw"
    short_description = "hw"

    @trace.trace
    def process(self, packet):
        LOG.info("HelloWorldPlugin")
        # fromcall = packet.get("from")
        # message = packet.get("message_text", None)
        # ack = packet.get("msgNo", "0")
        reply = (
            "Hello World!"
        )
        return reply.rstrip()

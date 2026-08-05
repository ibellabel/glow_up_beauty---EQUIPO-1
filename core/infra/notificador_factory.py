import os


class Notificador:
    def enviar_confirmacion(self, orden):
        raise NotImplementedError


class EmailNotificador(Notificador):
    def enviar_confirmacion(self, orden):
        print(f"[EMAIL REAL] Confirmación enviada para orden #{orden.id}")


class ConsolaNotificador(Notificador):
    def enviar_confirmacion(self, orden):
        print(f"[DEV] Orden #{orden.id} creada (simulado).")


class NotificadorFactory:
    @staticmethod
    def crear():
        env = os.environ.get("ENV_TYPE", "DEV")
        if env == "REAL":
            return EmailNotificador()
        return ConsolaNotificador()
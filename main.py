import tkinter as tk
from discord_webhook import DiscordWebhook, DiscordEmbed

def handle_focus_in(_):
    webhookinput.delete(0, tk.END)
    webhookinput.config(fg='black')

def handle_focus_out(_):
    webhookinput.delete(0, tk.END)
    webhookinput.config(fg='grey')
    webhookinput.insert(0, " Webhook here")


root = tk.Tk()


webhookinput = tk.Entry(root, bg='white', width=30, fg='grey')
webhookinput.grid(row=0, column=0, pady=15, columnspan=2)

webhookinput.insert(0, "webhook here")

webhookinput.bind("<FocusIn>", handle_focus_in)
webhookinput.bind("<FocusOut>", handle_focus_out)

def click():
    webhookurl = webhookinput.get()
    webhook = DiscordWebhook(
        url=webhookurl,
        username="testnn")

    embed = DiscordEmbed(title="title", description="description", color='6a329f')
    embed.set_timestamp()

    webhook.add_embed(embed)
    response = webhook.execute()
    webhooksucces = "action complete"
    return webhooksucces

myButton = tk.Button(root, text="SEND", command = click, fg="blue", bg = "red").grid(row=3, column=0)




root.mainloop()


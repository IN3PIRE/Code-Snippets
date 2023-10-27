const { SlashCommandBuilder } = require('@discordjs/builders');
const { Permissions, EmbedBuilder } = require('discord.js');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('purge')
    .setDescription('Delete messages in a channel')
    .addIntegerOption((option) =>
      option
        .setName('amount')
        .setDescription('The number of messages to delete (1-100)')
        .setRequired(true)
    ),
  async execute(interaction) {
    const amount = interaction.options.getInteger('amount');

    // Check if the user has the MANAGE_MESSAGES permission
    if (!interaction.member.permissions.has(Permissions.FLAGS.MANAGE_MESSAGES)) {
      return interaction.reply({
        content: 'You do not have permission to use this command.',
        ephemeral: true,
      });
    }

    // Validate the amount
    if (amount < 1 || amount > 100) {
      return interaction.reply({
content: 'Please enter a valid number between 1 and 100.',
        ephemeral: true,
      });
    }

    // Check if the bot has the MANAGE_MESSAGES permission
    if (!interaction.guild.me.permissions.has(Permissions.FLAGS.MANAGE_MESSAGES)) {
      return interaction.reply({
        content:
          'I do not have the necessary permissions to delete messages in this channel.',
        ephemeral: true,
      });
    }

    try {
      const messages = await interaction.channel.messages.fetch({ limit: amount });
      await interaction.channel.bulkDelete(messages, true);

      const successEmbed = new EmbedBuilder()
        .setColor('#00ff00')
        .setDescription(`Successfully deleted ${amount} messages.`);

      return interaction.reply({
        embeds: [successEmbed],
        ephemeral: true,
      });
    } catch (error) {
      console.error(error);
      return interaction.reply({
        content: 'An error occurred while deleting the messages.',
        ephemeral: true,
      });
    }
  },
};

const { SlashCommandBuilder } = require('discord.js');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('purge')
    .setDescription('Purge messages with optional filters')
    .addIntegerOption((option) =>
      option.setName('amount')
      .setDescription('Number of messages to purge')
      .setRequired(false)
    )
    .addStringOption((option) =>
      option.setName('filter')
      .setDescription('Filter options: bots, users, attachments, embeds, mentions')
      .setRequired(false)
    ),

  async execute(interaction) {
    if (!interaction.member.permissions.has('ManageMessages')) {
      return interaction.reply({ content: 'You do not have permission to use this command.', ephemeral: true });
    }

    const amount = interaction.options.getInteger('amount') || 10;
    const filterOption = interaction.options.getString('filter');

    let filter = (msg) => true;
    if (filterOption) {
      switch (filterOption) {
        case 'bots':
          filter = (msg) => msg.author.bot;
          break;
        case 'users':
          filter = (msg) => !msg.author.bot;
          break;
        case 'attachments':
          filter = (msg) => msg.attachments.size > 0;
          break;
        case 'embeds':
          filter = (msg) => msg.embeds.length > 0;
          break;
        case 'mentions':
          filter = (msg) => msg.mentions.users.size > 0;
          break;
        default:
          return interaction.reply({ content: 'Invalid filter option.', ephemeral: true });
      }
    }

    try {
      const messages = await interaction.channel.messages.fetch({ limit: amount });
      const filteredMessages = messages.filter(filter);

      await interaction.channel.bulkDelete(filteredMessages);
      interaction.reply(`Successfully purged ${filteredMessages.size} messages.`);
    } catch (error) {
      console.error(error);
      interaction.reply({ content: 'Failed to purge messages.', ephemeral: true });
    }
  },
};

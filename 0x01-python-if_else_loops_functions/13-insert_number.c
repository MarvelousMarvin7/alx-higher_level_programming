#include "lists.h"

/**
 * insert_node - insert a node in a sorted linked list
 * @head: head of list
 * @number: number to insert
 * Return: Address of new node else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t  *temp, *new_node, *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	temp = *head;
	prev = NULL;

	new_node->n = number;
	new_node->next = NULL;

	if (temp == NULL || temp->n >= number)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}

	while (temp != NULL && temp->n < number)
	{
		prev = temp;
		temp = temp->next;
	}
	new_node->next = temp;
	prev->next = new_node;
	return (new_node);
}

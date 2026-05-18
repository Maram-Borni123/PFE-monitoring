# Projet PFE — Plateforme de Monitoring DevOps

## Présentation du projet

Ce projet de fin d’études a pour objectif de concevoir et de déployer une plateforme centralisée de monitoring et de collecte de logs dans un environnement DevOps.

La solution permet de :

- Collecter les métriques système et applicatives ;
- Centraliser les logs provenant de plusieurs serveurs ;
- Visualiser les données à travers des tableaux de bord ;
- Déclencher des alertes automatiques ;
- Automatiser entièrement le déploiement de l’infrastructure.

## Technologies utilisées

- Vagrant
- Ansible
- Docker Compose
- Prometheus
- Grafana
- Loki
- Promtail
- Alertmanager
- Blackbox Exporter
- Node Exporter
- cAdvisor

## Architecture de la solution

Le projet s’appuie sur plusieurs machines virtuelles déployées avec Vagrant.

| VM | Adresse IP | Rôle |
|----|------------|------|
| monitoring | 10.10.10.50 | Serveur central de monitoring |
| os-linux | 10.10.10.51 | Serveur Linux supervisé |
| webserver | 10.10.10.52 | Serveur web |
| database | 10.10.10.53 | Serveur MariaDB |
| nosql | 10.10.10.54 | Serveur MongoDB |
| appjava | 10.10.10.55 | Application Java |
| appscript | 10.10.10.56 | Scripts applicatifs |
| application-services | 10.10.10.57 | Services applicatifs |

## Structure du projet

```text
projet-pfe/
├── Vagrantfile
├── ansible/
│   ├── inventory/
│   ├── playbooks/
│   ├── roles/
│   └── group_vars/
├── monitoring-stack/
├── web/
├── db_monitoring/
├── datastore-stack/
├── appjava-stack/
└── monitoring-app/
```

## Prérequis

Avant de démarrer le projet, les outils suivants doivent être installés :

- VirtualBox
- Vagrant
- Ansible
- Docker
- Docker Compose

## Déploiement des machines virtuelles

```bash
vagrant up
```

Vérification de l’état des machines :

```bash
vagrant status
```

## Déploiement automatisé avec Ansible

```bash
ansible-playbook -i ansible/inventory/hosts.ini ansible/playbooks/deploy_agent.yml
```

Ce playbook :

1. Vérifie que les machines virtuelles sont démarrées ;
2. Installe Docker et Docker Compose ;
3. Déploie les agents de monitoring ;
4. Met à jour la configuration de Prometheus ;
5. Recharge Prometheus.

## Démarrage manuel de la stack de monitoring

```bash
cd monitoring-stack
docker compose up -d
```

## Accès aux interfaces web

| Service | URL |
|--------|-----|
| Grafana | http://10.10.10.50:3000 |
| Prometheus | http://10.10.10.50:9090/prometheus/ |
| Loki | http://10.10.10.50:3100 |
| Alertmanager | http://10.10.10.50:9093/alertmanager/ |

## Fonctionnalités principales

### Monitoring des métriques

- Utilisation CPU, mémoire, disque et réseau ;
- Supervision des conteneurs Docker ;
- Monitoring de MariaDB, MongoDB et JVM ;
- Vérification de disponibilité via Blackbox Exporter.

### Centralisation des logs

- Logs système ;
- Logs Docker ;
- Logs Nginx, Apache et Varnish ;
- Logs applicatifs.

### Alerting

- Alertes sur CPU, mémoire et disque ;
- Détection des services indisponibles ;
- Notifications par e-mail.

### Sécurité

- Reverse proxy Nginx avec HTTPS ;
- Pare-feu UFW ;
- Scan de vulnérabilités avec Trivy.

## Scan de vulnérabilités

```bash
docker compose run --rm trivy
```

## Dépannage

### Vérifier les conteneurs

```bash
docker ps
```

### Consulter les logs

```bash
docker logs prometheus
docker logs grafana
docker logs loki
docker logs promtail
docker logs alertmanager
```

### Vérifier un exporter

```bash
curl http://localhost:9100/metrics
```

## Améliorations futures

- Déploiement sur Kubernetes ;
- Haute disponibilité ;
- Intégration avec Slack ou Microsoft Teams ;
- Stockage longue durée avec Thanos.

## Auteur

**Borni Maram**  
Projet de Fin d’Études — Licence en Ingénierie des Systèmes Informatiques  
Année universitaire 2025–2026

## Encadrement

- Encadrant professionnel : M. Zied Tlili
- Encadrant académique : M. Med Anis Loghmari
- Entreprise d’accueil : MEDIANET

## Licence

Ce projet a été réalisé dans le cadre d’un projet de fin d’études.
